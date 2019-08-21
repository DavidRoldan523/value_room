from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status
from ..connection.brandwatch_connection import BrandWatchConnection
from ..connection import credentials as credential


def remove_all_whitespaces(sentence):
    return ''.join(sentence.split())


@api_view(['POST'])
def get_token(request):
    try:
        token = BrandWatchConnection(credential.username, credential.password).connect()
        url = 'https://api.brandwatch.com/projects/summary'
        response = requests_python.get(url, headers={'Authorization': f'Bearer {token}'})
        return Response(response.json(), status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)
