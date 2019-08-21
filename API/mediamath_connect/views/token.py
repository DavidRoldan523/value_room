import requests as python_requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..connection import credentials as credential


@api_view(['POST'])
def get_token(request):
    try:
        #Data
        data = {'grant_type' : 'password',
                'username' : credential.username,
                'password' : credential.password,
                'audience' : 'https://api.mediamath.com/',
                'scope' : '',
                'client_id' : credential.client_id,
                'client_secret' : credential.client_secret}
        response = python_requests.post('https://auth.mediamath.com/oauth/token', data=data)
        """
        response = python_requests.post('https://api.mediamath.com/api/v2.0/session', 
                                        headers={'Authorization': credential.access_token})
        print(response.text)
        """
        

        return Response(response, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)
