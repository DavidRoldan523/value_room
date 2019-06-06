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
            temp_comment = {'video_id': comment['snippet']['videoId'],
                            'comment_id': comment['snippet']['topLevelComment']['id'],
                            'comment': comment['snippet']['topLevelComment']['snippet']['textOriginal'],
                            'created_time': comment['snippet']['topLevelComment']['snippet']['publishedAt']}
            response_final.append(temp_comment)


@api_view(['POST'])
def get_videos_comments(request):
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
                        f"&fields=items(snippet(videoId,topLevelComment(id,snippet(textOriginal,publishedAt))))" \
                        f"&videoId={video['id']['videoId']}" \
                        f"&key={key}" \
                        f"&maxResults=100" \
                        f"&moderationStatus=published" \
                        f"&textFormat=plainText"
            url_comments_list.append(url_video)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_site, url_comments_list)

        return Response(response_final, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': f'URL incorrecto: {e}'}, status.HTTP_400_BAD_REQUEST)

