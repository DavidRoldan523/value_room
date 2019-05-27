from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status

@api_view(['POST'])
def get_reviews_posts(request):
    try:
        token = request.data.get('token')
        adaccount_id = request.data.get('adaccount_id')
        fields = request.data.get('fields') # name,account_id,buying_type,effective_status,start_time,stop_time
        url = f"https://graph.facebook.com/v3.3/act_{adaccount_id}/campaigns/" \
            f"?access_token={token}" \
            f"&fields={fields}"
        response = requests_python.get(url)
        return Response(response.json(), status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)