from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status
import concurrent.futures
import threading
import re
from .tools.token import Token

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


def replace_quotes(string):
    string = re.sub(r"“", '', string)
    string = re.sub(r"”", '', string)
    string = re.sub('\n', ' ', string)
    return string


@api_view(['POST'])
def get_comments(request):
    try:
        global response_crude
        response_crude = []
        page_id = request.data.get('page_id')
        since = request.data.get('since')
        until = request.data.get('until')
        fb_token = Token().get_fb_token()
        url_posts = f"https://graph.facebook.com/v4.0/{page_id}/posts" \
                    f"?access_token={fb_token}" \
                    f"&fields=id,created_time,from,message" \
                    f"&since={since}&until={until}&limit=100"
        response_posts = requests_python.get(url_posts)
        response_posts_json = response_posts.json()
        response_final_posts = [{'page_name': '',
                                 'page_id': '',
                                 'since': '',
                                 'until': '',
                                 'results': []}]
        if len(response_posts_json['data']) != 0:
            page_name = ''
            for post in response_posts_json['data']:
                try:
                    temp_id = post['id'].split('_')
                    date_temp = post['created_time'].split('T')
                    page_name = post['from']['name']
                    temp_post = {'post_id': temp_id[1],
                                'post_name': replace_quotes(post['message']),
                                'created_time': date_temp[0],
                                'comments': []}
                    response_final_posts[0]['results'].append(temp_post)
                except Exception as e:
                    pass
        else:
            return Response({}, status.HTTP_400_BAD_REQUEST)


        response_final_posts[0]['page_name'] = page_name
        response_final_posts[0]['page_id'] = page_id
        response_final_posts[0]['since'] = since
        response_final_posts[0]['until'] = until


        url_comments_list = []
        for post in response_posts_json['data']:
            url_temp = f"https://graph.facebook.com/v3.3/{post['id']}/comments" \
                    f"?access_token={fb_token}" \
                    f"&fields=message,created_time&limit=500"
            url_comments_list.append(url_temp)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_site, url_comments_list)



        response_clean = []
        response_clean.append([dict_temp for dict_temp in response_crude if dict_temp['message'] != ""])
        for post in response_final_posts[0]['results']:
            for comment in response_clean[0]:
                temp_id = comment['id'].split('_')
                date_temp = post['created_time'].split('T')
                if post['post_id'] == temp_id[0]:
                    dict_temp = {'comment_id': temp_id[1],
                                 'comment_text': replace_quotes(comment['message']),
                                 'created_time': date_temp[0]}
                    post['comments'].append(dict_temp)


        return Response(response_final_posts, status.HTTP_200_OK)
    except:
        return Response({}, status.HTTP_400_BAD_REQUEST)