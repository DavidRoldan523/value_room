import concurrent.futures
import threading
import random
import urllib3
import csv

from rest_framework.decorators import api_view
from rest_framework.response import Response
from requests import get
from lxml import html
from rest_framework import status


response_crude = []
thread_local = threading.local()
headers = {}


def parse_month_to_number(month):
    return { 
        'jan':  '01', 
        'feb':  '02', 
        'mar':  '03',
        'apr':  '04',
        'may':  '05',
        'jun':  '06',
        'jul':  '07',
        'aug':  '08',
        'sep':  '09',
        'oct':  '10',
        'nov':  '11',
        'dec':  '12',
    }.get(month, "Invalid date")


def parse_json_to_csv(name, json):
    with open(f"{name}.csv", mode='w', newline='', encoding="utf-8") as file:
        employee_writer = csv.writer(file, delimiter='|')
        employee_writer.writerow(json[0].keys())
        for data in json:
            employee_writer.writerow(data.values())


def get_random_user_agent():
    user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
                       'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36']
    return random.choice(user_agent_list)


def download_site(url):
    global response_crude, headers
    urllib3.disable_warnings()
    response = get(url, headers=headers, verify=False, timeout=20)
    cleaned_response = response.text.replace('\x00', '')
    parser_to_html = html.fromstring(cleaned_response)
    reviews = parser_to_html.xpath('.//div[@class="comments-list comments-list--paginated"]')
    for review in reviews[0]:
        review_text = review.xpath('.//div[@class="comment-body"]//text()')
        review_author = review.xpath('.//div[@class="lbox--v-3 flex--toW3 height--toW3-auto"]//text()')
        review_date = review.xpath('.//time[@class="text--color-greyShade overflow--wrap-off"]//text()')
        review_date_clean = (review_date[0][:len(review_date[0]) - 1]).split(' ')
        review_dict = {'review_text': (review_text[0]).replace('"', ''),
                       'review_author': review_author[0],
                       'review_date': f'{review_date_clean[1]}-{parse_month_to_number(review_date_clean[0])}-2019'}
        response_crude.append(review_dict)


@api_view(['POST'])
def get_reviews(request):
    try:
        global response_crude, headers
        url_initial = "https://www.promodescuentos.com/ofertas/" \
                      "gillette-mach3-gratis-contestando-encuesta-323386" \
                      "#thread-comments"
        urllib3.disable_warnings()
        headers = {'User-Agent': get_random_user_agent()}
        response_initial = get(url_initial, headers=headers, verify=False, timeout=30)
        cleaned_response = response_initial.text.replace('\x00', '')
        parser_to_html = html.fromstring(cleaned_response)

        total_reviews = ''.join(parser_to_html.xpath('.//div[@class="lbox--v-4"]//span[@class="space--l-2"]//text()')).strip().replace(' Comentarios', '')

        url_comments_list = []
        for page in range(1, int(int(total_reviews) / 20) + 2):
            url_temp = f"https://www.promodescuentos.com/ofertas/" \
                       f"gillette-mach3-gratis-contestando-encuesta-323386" \
                       f"?page={page}" \
                       f"#thread-comments"
            url_comments_list.append(url_temp)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_site, url_comments_list)

        parse_json_to_csv('test', response_crude)
        return Response({'Response': 'Download the file in root directory'}, status.HTTP_200_OK)
        # return Response(response_crude, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': f'URL incorrecto: {e}'}, status.HTTP_400_BAD_REQUEST)