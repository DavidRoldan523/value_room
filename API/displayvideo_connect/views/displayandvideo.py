import os
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..connection import credentials as credential
from ..connection.displayvideo_connection import DisplayVideoConnect


def remove_all_whitespaces(sentence):
  return ''.join(sentence.split())


@api_view(['POST'])
def get_report(request):
  try:
    query_id = remove_all_whitespaces(request.data.get('query_id'))
    system_file_location = os.path.dirname(__file__).replace('/views', '')
    connection = DisplayVideoConnect(system_file_location +
                                     credential.key_file_location,
                                     credential.scopes).connect()
    response = connection.queries().getquery(queryId=query_id).execute()
    return Response(response, status.HTTP_200_OK)
  except Exception as e:
    return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)
