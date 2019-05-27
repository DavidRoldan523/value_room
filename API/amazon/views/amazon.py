import json
import urllib3
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from lxml import html
from json import loads
from requests import get
from dateutil import parser as dateparser_to_html
import concurrent.futures

review_total_pages = []
headers = {}

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
    global review_total_pages, headers
    urllib3.disable_warnings()
    response = get(url, headers=headers, verify=False, timeout=20)
    cleaned_response = response.text.replace('\x00', '')
    parser_to_html = html.fromstring(cleaned_response)
    reviews = parser_to_html.xpath('//div[contains(@id,"reviews-summary")]')
    if not reviews:
        reviews = parser_to_html.xpath('//div[@data-hook="review"]')
    for review in reviews:
        raw_review_author = review.xpath('.//span[contains(@class,"profile-name")]//text()')
        raw_review_rating = review.xpath('.//i[@data-hook="review-star-rating"]//text()')
        raw_review_header = review.xpath('.//a[@data-hook="review-title"]//text()')
        raw_review_posted_date = review.xpath('.//span[@data-hook="review-date"]//text()')
        raw_review_text1 = review.xpath('.//span[@data-hook="review-body"]//text()')
        raw_review_text2 = review.xpath(
            './/div//span[@data-action="columnbalancing-showfullreview"]/@data-columnbalancing-showfullreview')
        raw_review_text3 = review.xpath('.//div[contains(@id,"dpReviews")]/div/text()')

        # Cleaning data
        author = ' '.join(' '.join(raw_review_author).split())
        review_rating = ''.join(raw_review_rating).replace('out of 5 stars', '')
        review_header = ' '.join(' '.join(raw_review_header).split())
        try:
            review_posted_date = dateparser_to_html.parse(''.join(raw_review_posted_date)).strftime('%d %b %Y')
        except:
            review_posted_date = None
        review_text = ' '.join(' '.join(raw_review_text1).split())

        # Grabbing hidden comments if present
        if raw_review_text2:
            json_loaded_review_data = loads(raw_review_text2[0])
            json_loaded_review_data_text = json_loaded_review_data['rest']
            cleaned_json_loaded_review_data_text = re.sub('<.*?>', '', json_loaded_review_data_text)
            full_review_text = review_text + cleaned_json_loaded_review_data_text
        else:
            full_review_text = review_text
        if not raw_review_text1:
            full_review_text = ' '.join(' '.join(raw_review_text3).split())

        review_dict = {
            'review_text': full_review_text,
            'review_posted_date': review_posted_date,
            'review_header': review_header,
            'review_rating': review_rating,
            'review_author': author
        }
        review_total_pages.append(review_dict)




def get_header(asin):
    try:
        global headers
        ratings_dict = {}
        amazon_url = 'https://www.amazon.com/product-reviews/' + asin + '/ref=cm_cr_arp_d_paging_btm_next_1?pageNumber=1'
        urllib3.disable_warnings()
        headers = {'User-Agent': get_random_user_agent()}
        response = get(amazon_url, headers=headers, verify=False, timeout=30)
        cleaned_response = response.text.replace('\x00', '')
        parser_to_html = html.fromstring(cleaned_response)

        data = {'number_reviews': ''.join(parser_to_html.xpath('.//span[@data-hook="total-review-count"]//text()')).replace(',', ''),
                'product_price': ''.join(parser_to_html.xpath('.//span[contains(@class,"a-color-price arp-price")]//text()')).strip(),
                'product_name': ''.join(parser_to_html.xpath('.//a[@data-hook="product-link"]//text()')).strip(),
                'total_ratings': parser_to_html.xpath('//table[@id="histogramTable"]//tr')}

        for ratings in data['total_ratings']:
            extracted_rating = ratings.xpath('./td//a//text()')
            if extracted_rating:
                rating_key = extracted_rating[0]
                rating_value = extracted_rating[1]
                if rating_key:
                    ratings_dict.update({rating_key: rating_value})

        number_page_reviews = int(int(data['number_reviews']) / 10)

        if number_page_reviews % 2 == 0:
            number_page_reviews += 1
        else:
            number_page_reviews += 2

        return data['product_price'], data['product_name'],\
               data['number_reviews'], ratings_dict, number_page_reviews, headers
    except Exception as e:
        return {"url": amazon_url, "error": e}


def get_all_reviews(asin):
    global review_total_pages
    url_list = []
    product_price, product_name, number_reviews, ratings_dict, stop_loop_for, headers = get_header(asin)
    for page_number in range(1, stop_loop_for):
        amazon_url = 'https://www.amazon.com/product-reviews/' + asin + '/ref=cm_cr_arp_d_paging_btm_next_' \
                     + str(page_number) + '?pageNumber=' + str(page_number)
        url_list.append(amazon_url)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_site, url_list)

    result = {
        'product_name': product_name,
        'product_price': product_price,
        'number_reviews': number_reviews,
        'ratings': ratings_dict,
        'reviews': review_total_pages,
    }
    return result


def create_json(name, data):
    with open(f'{name}.json', 'w') as outfile:
        json.dump(data, outfile)



@api_view(['POST'])
def get_reviews(request):
    try:
        response = []
        asin_list = (request.data.get('asin').replace(' ', '')).split(',')
        format = (request.data.get('format').strip()).lower()
        file_name = (request.data.get('format').strip()).lower()
        for asin in asin_list:
            print(f"In Proces for {asin}")
            temp = get_all_reviews(asin)
            response.append(temp)

        if format != 'json':
            return Response(response, status.HTTP_200_OK)
        else:
            create_json(file_name, response)
            return Response({"Success": "Download the JSON in root Directory"}, status.HTTP_200_OK)

    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)