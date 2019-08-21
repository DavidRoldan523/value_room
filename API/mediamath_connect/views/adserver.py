import json as json_python
from ast import literal_eval

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..connection import credentials as credential
from ..connection.mediamath_connection import MediaMathConnection


@api_view(['GET'])
def get_adservers(request):
    try:
        connection = MediaMathConnection(credential.username,
                                         credential.password).connect()
        adservers = connection.get("ad_servers")
        response = []
        for adserver in adservers:
            response.append(literal_eval("{'name': '" + str(adserver.name) +
                                         "', 'id': '" + str(adserver.id) +
                                         "', '_type': '" + str(adserver._type) + "'}"))

        return Response(response, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_one_adserver(request, pk):
    try:
        id_adserver = pk
        response = []
        connection = MediaMathConnection(credential.username,
                                         credential.password).connect()
        adserver = connection.get("ad_servers", id_adserver)

        response.append(literal_eval("{'name': '" + str(adserver.name) +
                                                 "', 'id': '" + str(adserver.id) +
                                                 "', 'version': '" + str(adserver.version) +
                                                 "', '_type': '" + str(adserver._type) + "'}"))
        return Response(response, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)