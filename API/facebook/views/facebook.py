from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status
import concurrent.futures
import threading

response_final = []
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests_python.Session()
    return thread_local.session


def download_site(url):
    print("ENTRE")
    global response_final
    session = get_session()
    with session.get(url) as response:
        response_final.append(response.json())


@api_view(['POST'])
def get_posts_id(request):
    try:
        global response_final
        token = request.data.get('token')
        page_id = request.data.get('page_id')
        fields = request.data.get('fields') #id,created_time
        since = request.data.get('since')
        until = request.data.get('until')
        url = f"https://graph.facebook.com/v3.3/{page_id}/posts" \
            f"?access_token={token}" \
            f"&fields={fields}" \
            f"&since={since}&until={until}&limit=100"
        response = requests_python.get(url)
        response_posts_id = response.json()
        url_list = []
        for post in response_posts_id['data']:
            url2 = f"https://graph.facebook.com/v3.3/{post['id']}/comments" \
                    f"?access_token={token}" \
                    f"&fields={fields},comments{{message,from}}&limit=500"
            url_list.append(url2)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_site, url_list)

        return Response(response_final, status.HTTP_200_OK)
    except Exception:
        return Response({'Error': 'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)