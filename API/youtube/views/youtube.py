from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status

@api_view(['POST'])
def get_reviews_video(request):
    try:
        video_id = request.data.get('video_id')
        key = request.data.get('key')
        url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet" \
            f"&videoId={video_id}" \
            f"&key={key}"
        response = requests_python.get(url)
        return Response(response.json(), status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)