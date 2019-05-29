from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status

@api_view(['POST'])
def get_accounts_id(request):
    try:
        token = request.data.get('token')
        page_id = request.data.get('page_id')
        url = f"https://graph.facebook.com/v3.3/{page_id}" \
            f"?access_token={token}" \
            f"&fields=instagram_business_account,username,instagram_accounts{{username}}"
        response = requests_python.get(url)    
        return Response(response.json(), status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_comments(request):
    try:
        token = request.data.get('token')
        account_ig_id = request.data.get('account_ig_id')
        fields = request.data.get('fields') #id,caption,username,media_url,media_type,timestamp,like_count
        url = f"https://graph.facebook.com/v3.3/{account_ig_id}/media" \
            f"?access_token={token}" \
            f"&fields=comments{{text}},{fields}&limit=500"
        response = requests_python.get(url)
        return Response(response.json(), status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)