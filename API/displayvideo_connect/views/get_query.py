import requests as requests_python
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..connection.refresh_token import DisplayVideoConnect
import json


def remove_all_whitespaces(sentence):
  return ''.join(sentence.split())


@api_view(['POST'])
def get_query(request):
  try:
    google_token = DisplayVideoConnect().connect()
    query_id = remove_all_whitespaces(request.data.get('query_id'))
    url = f'https://www.googleapis.com/doubleclickbidmanager/v1/query/{query_id}'            
    response = requests_python.get(url, headers={'Authorization': f'Bearer {google_token}'})
    return Response(response.json(), status.HTTP_200_OK)
  except Exception as e:
      return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)