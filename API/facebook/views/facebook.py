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
        response2 = response.json()
        url_list = []
        print("llegue")
        for post in response2['data']:
            url2 = f"https://graph.facebook.com/v3.3/{post['id']}/comments" \
                f"?access_token={token}" \
                f"&fields={fields},comments{{message,from}}&limit=500"
            url_list.append(url2)
        print(url_list)
        return Response({"hello":"world"}, status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)