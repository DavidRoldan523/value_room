from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status

@api_view(['POST'])
def get_posts(request):
    try:
        token = request.data.get('token')
        page_id = request.data.get('page_id')
        url_posts = f"https://graph.facebook.com/v3.3/{page_id}/media" \
            f"?access_token={token}" \
            f"&fields=id,caption,timestamp&limit=500"
        response = requests_python.get(url_posts)
        response_crude = response.json()
        response_final = []
        for post in response_crude['data']:
            dict_temp = {'id_post': post['id'],
                        'name_post': post['caption'],
                        'created_time': post['timestamp']}
            response_final.append(dict_temp)
        return Response(response_final, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': f'URL incorrecto: {e}'}, status.HTTP_400_BAD_REQUEST)