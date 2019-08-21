import json as json_python
from ast import literal_eval

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..connection import credentials as credential
from ..connection.mediamath_connection import MediaMathConnection


def obtain_status(status):
    if (str(status).lower()) == 'true':
        status_request = True
    else:
        status_request = False
    return status_request


@api_view(['GET', 'POST'])
def get_videocreatives(request):
    if request.method == 'GET':
        try:
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            videocreatives = connection.get("atomic_creatives")
            response = []
            print(videocreatives[0])
            for videocreative in videocreatives:

                response.append(literal_eval("{'name': '" + str(videocreative.name) +
                                             "', 'id': '" + str(videocreative.id) +
                                             "', '_type': '" + str(videocreative._type) + "'}"))

            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        try:
            pass
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def get_one_videocreative(request, pk):
    if request.method == 'GET':
        try:
            print("entre")
            id_videocreative = pk
            response = []
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            videocreative = connection.get("variants", id_videocreative)
            print(videocreative)
            """
            response.append(literal_eval("{'autoVendors': '" + str(videocreative.autoVendors) +
                                         "', 'companionlds': '" + str(videocreative.companionlds) +
                                         "', 'details': '" + str(videocreative.details) +
                                         "', 'duration': '" + str(videocreative.duration) +
                                         "', 'isAudio': '" + str(videocreative.isAudio) +
                                         "', 'isSecure': '" + str(videocreative.isSecure) +
                                         "', 'isUploaded': '" + str(videocreative.isUploaded) +
                                         "', 'percent': '" + str(videocreative.percent) +
                                         "', 'readyToServe': '" + str(videocreative.readyToServe) +
                                         "', 'status': '" + str(videocreative.status) +
                                         "', 'unsecureUrls': '" + str(videocreative.unsecureUrls) +
                                         "', 'vastVersion': '" + str(videocreative.vastVersion) + "'}"))"""
            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            pass
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)


