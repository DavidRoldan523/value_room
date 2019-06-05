from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status
import concurrent.futures
import threading

response_crude = []
thread_local = threading.local()


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
        token = request.data.get('token')
        page_id = request.data.get('page_id')
        url_posts = f"https://graph.facebook.com/v3.3/{page_id}/media" \
            f"?access_token={token}" \
            f"&fields=id&limit=500"
        response_posts = requests_python.get(url_posts)
        response_posts_json = response_posts.json()
        url_comments_list = []
        for post in response_posts_json['data']:
            url_temp = f"https://graph.facebook.com/v3.3/{post['id']}/comments" \
                f"?access_token={token}" \
                f"&fields=id,media,text,timestamp&limit=500"
            url_comments_list.append(url_temp)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_site, url_comments_list)

        response_clean = []
        response_clean.append([dict_temp for dict_temp in response_crude if dict_temp['text'] != ""])
        response_final = []
        for comment in response_clean[0]:
            dict_temp = {'id_post': comment['media']['id'],
                         'id_comment': comment['id'],
                         'comment': comment['text'],                
                         'created_time': comment['timestamp']}
            response_final.append(dict_temp)

        return Response(response_final, status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)