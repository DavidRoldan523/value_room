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
    global response_final
    session = get_session()
    with session.get(url) as response:
        response_temp = response.json()
        for comment in response_temp['items']:
            response_final.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])


@api_view(['POST'])
def get_reviews_videos(request):
    try:
        global response_final
        channel_id = request.data.get('channel_id')
        key = request.data.get('key')
        date = request.data.get('date')
        url_video = f"https://www.googleapis.com/youtube/v3/search" \
                    f"?key={key}&channelId={channel_id}" \
                    f"&part=id" \
                    f"&order=date" \
                    f"&maxResults=50" \
                    f"&publishedAfter={date}"  # (RFC 3339) DATE FORMAT
        response_videos = requests_python.get(url_video)
        response_videos_json = response_videos.json()
        url_comments_list = []
        for video in response_videos_json['items']:
            url_video = f"https://www.googleapis.com/youtube/v3/commentThreads" \
                        f"?part=snippet" \
                        f"&videoId={video['id']['videoId']}" \
                        f"&key={key}" \
                        f"&maxResults=100" \
                        f"&moderationStatus=published" \
                        f"&textFormat=plainText"
            url_comments_list.append(url_video)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_site, url_comments_list)

        return Response(response_final, status.HTTP_200_OK)
    except Exception:
        return Response({'Error': 'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)

