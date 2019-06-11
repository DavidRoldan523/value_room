from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status


@api_view(['POST'])
def get_token(request):
    try:
        previus_token = request.data.get('previus_token')
        url_posts = f"https://graph.facebook.com/oauth/access_token?client_id=272278490387976" \
            f"&client_secret=817e43a3a93beb7da194c28a7013950d&grant_type=fb_exchange_token&fb_exchange_token={previus_token}"
        response_posts = requests_python.get(url_posts)
        response_final = response_posts.json()


        return Response({'Response': response_final['access_token']}, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': f'URL incorrecto: {e}'}, status.HTTP_400_BAD_REQUEST)