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
def get_posts_embedded(request):
    try:
        global response_crude
        token = request.data.get('token')
        page_id = request.data.get('page_id')
        since = request.data.get('since')
        until = request.data.get('until')
        url_posts = f"https://graph.facebook.com/v3.3/{page_id}/posts" \
                    f"?access_token={token}" \
                    f"&fields=id,created_time,from" \
                    f"&since={since}&until={until}&limit=100"
        response_posts = requests_python.get(url_posts)
        response_posts_json = response_posts.json()
        response_final_posts = []

        for post in response_posts_json['data']:
            temp_id = post['id'].split('_')
            temp_post = { 'page_name': post['from']['name'],
                          'page_id': temp_id[0],
                          'post_id': temp_id[1],
                          'created_time': post['created_time'],
                          'comments': []}
            response_final_posts.append(temp_post)

        url_comments_list = []
        for post in response_posts_json['data']:
            url_temp = f"https://graph.facebook.com/v3.3/{post['id']}/comments" \
                    f"?access_token={token}" \
                    f"&fields=message,created_time&limit=500"
            url_comments_list.append(url_temp)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_site, url_comments_list)

        response_clean = []
        response_clean.append([dict_temp for dict_temp in response_crude if dict_temp['message'] != ""])
        for post in response_final_posts:
            for comment in response_clean[0]:
                temp_id = comment['id'].split('_')
                if post['post_id'] == temp_id[0]:                    
                    dict_temp = {'comment_id': temp_id[1],
                                'comment_text': comment['message'],                
                                'created_time': comment['created_time']}                    
                    post['comments'].append(dict_temp)

        return Response(response_final_posts, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': f'URL incorrecto: {e}'}, status.HTTP_400_BAD_REQUEST)