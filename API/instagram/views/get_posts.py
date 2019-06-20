from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status
import concurrent.futures
import threading
from datetime import date as python_date

response_crude = []
thread_local = threading.local()


def get_fb_token(previus_token):
    url_posts = f"https://graph.facebook.com/oauth/access_token?client_id=272278490387976" \
                f"&client_secret=817e43a3a93beb7da194c28a7013950d" \
                f"&grant_type=fb_exchange_token" \
                f"&fb_exchange_token={previus_token}"
    response = requests_python.get(url_posts)
    token = response.json()
    return token['access_token']


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests_python.Session()
    return thread_local.session


def download_site(url):
    global response_crude
    session = get_session()
    with session.get(url) as response:
        temp = response.json()
        response_crude += temp['data']


@api_view(['POST'])
def get_comments(request):
    try:
        global response_crude
        response_crude = []
        page_id = request.data.get('page_id')
        fb_token = get_fb_token('EAAD3osazFggBAO3y3V6olXlnM1yLeGQa6hWE2TEmH9XIM92pg4g6Ee6CZBf094sw1HHZCAK73cZC03pzxIrZACFr1FtzBbA0dSmRGMACzbEY23otq7upXWXPYubU3wLGLho3jGIKIcOe356dZCaWtkf2SZCicRx8YQiQILlh2COQZDZD')
        url_posts = f"https://graph.facebook.com/v3.3/{page_id}/media" \
                    f"?access_token={fb_token}" \
                    f"&fields=id,caption,timestamp,username&limit=500"
        response_posts = requests_python.get(url_posts)
        response_posts_json = response_posts.json()
        response_final_posts = []

        for post in response_posts_json['data']:
            date_temp = post['timestamp'].split('T')
            page_name = post['username']
            temp_post = {'post_id': post['id'],
                         'post_name': post['caption'],
                         'created_time': date_temp[0],
                         'comments': []}
            response_final_posts.append(temp_post)
        

        url_comments_list = []
        for post in response_posts_json['data']:
            url_temp = f"https://graph.facebook.com/v3.3/{post['id']}/comments" \
                        f"?access_token={fb_token}" \
                        f"&fields=id,media,text,timestamp&limit=500"
            url_comments_list.append(url_temp)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_site, url_comments_list)

        

        response_clean = []
        response_clean.append([dict_temp for dict_temp in response_crude if dict_temp['text'] != ""])
        
        for post in response_final_posts:
            for comment in response_clean[0]:
                if post['post_id'] == comment['media']['id']:
                    date_temp = comment['timestamp'].split('T')              
                    dict_temp = {'comment_id': comment['id'],
                                'comment_text': comment['text'],                
                                'created_time': date_temp[0]}                    
                    post['comments'].append(dict_temp)

        response_definitive = [{'page_name': '',
                                'page_id': '',
                                'since': '',
                                'until': '',
                                'results': []}]
        response_definitive[0]["page_name"] = page_name
        response_definitive[0]["page_id"] = page_id
        response_definitive[0]["since"] = date_temp[0]
        response_definitive[0]["until"] = python_date.today().strftime("%Y-%m-%d")
        response_definitive[0]['results'] = [post for post in response_final_posts if len(post['comments']) != 0]
        return Response(response_definitive, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': f'URL incorrecto: {e}'}, status.HTTP_400_BAD_REQUEST)