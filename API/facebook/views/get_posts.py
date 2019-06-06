from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status

@api_view(['POST'])
def get_posts(request):
    try:
        token = request.data.get('token')
        page_id = request.data.get('page_id')
        fields = request.data.get('fields') #id,created_time
        since = request.data.get('since')
        until = request.data.get('until')
        url_posts = f"https://graph.facebook.com/v3.3/{page_id}/posts" \
                    f"?access_token={token}" \
                    f"&fields={fields}" \
                    f"&since={since}&until={until}&limit=100"
        response_posts = requests_python.get(url_posts)
        response_crude = response_posts.json()
        response_final = []
        for comment in response_crude['data']:
            temp_id = comment['id'].split('_')
            dict_temp = {'id_page': temp_id[0],
                         'id_post': temp_id[1],
                         'name_post': comment['message'],
                         'created_time': comment['created_time']}
            response_final.append(dict_temp)

        return Response(response_final, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': f'URL incorrecto: {e}'}, status.HTTP_400_BAD_REQUEST)