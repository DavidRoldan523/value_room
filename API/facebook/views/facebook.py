from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status

@api_view(['POST'])
def get_posts_id(request):
    try:
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
        return Response(response.json(), status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_reviews_by_id_post(request):
    try:
        token = request.data.get('token')
        post_id = request.data.get('post_id')
        fields = request.data.get('fields') # created_time,message
        url = f"https://graph.facebook.com/v3.3/{post_id}/comments" \
            f"?access_token={token}" \
            f"&fields={fields},comments{{message,from}}&limit=500"
        response = requests_python.get(url)
        return Response(response.json(), status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)