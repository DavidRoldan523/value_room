from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status


@api_view(['POST'])
def get_videos(request):
    try:
        channel_id = request.data.get('channel_id')
        key = request.data.get('key')
        date = request.data.get('date')
        url_video = f"https://www.googleapis.com/youtube/v3/search" \
                    f"?key={key}&channelId={channel_id}" \
                    f"&part=id,snippet" \
                    f"&fields=items(snippet(publishedAt,title),id(videoId))" \
                    f"&order=date" \
                    f"&maxResults=50" \
                    f"&publishedAfter={date}"  # (RFC 3339) DATE FORMAT
        response_videos = requests_python.get(url_video)
        response_videos.encoding = "utf-8"
        response_videos_json = response_videos.json()
        response_final = []
        for video in response_videos_json['items']:
            temp_video = {'video_id': video['id']['videoId'],
                          'video_title': video['snippet']['title'],
                          'created_time': video['snippet']['publishedAt']}
            response_final.append(temp_video)

        return Response(response_final, status.HTTP_200_OK)
    except Exception:
        return Response({'Error': 'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)

