from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status

@api_view(['POST'])
def get_reviews_all_videos(request):
    try:
        channel_id = request.data.get('channel_id')
        key = request.data.get('key')
        url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet" \
            f"&allThreadsRelatedToChannelId={channel_id}" \
            f"&key={key}"
        response = requests_python.get(url)
        return Response(response.json(), status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)