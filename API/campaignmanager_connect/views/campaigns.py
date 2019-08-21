import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..connection import credentials as credential
from ..connection.campaignmanager_connection import CampaignManagerConnect


def remove_all_whitespaces(sentence):
    return ''.join(sentence.split())


@api_view(['POST'])
def get_campaigns(request):
    try:
        # profile_id = remove_all_whitespaces(request.data.get('profile_id'))
        system_file_location = os.path.dirname(__file__).replace('/views', '')
        connection = CampaignManagerConnect(system_file_location +
                                            credential.key_file_location,
                                            credential.scopes).connect()
        request = connection.userProfiles().list()
        response = request.execute()
        return Response(response, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)
