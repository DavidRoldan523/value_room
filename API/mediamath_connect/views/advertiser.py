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
def get_advertisers(request):
    if request.method == 'GET':
        try:
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            advertisers = connection.get("advertisers")
            response = []
            for advertiser_one in advertisers:
                advertiser = connection.get("advertisers", advertiser_one.id)
                response.append(literal_eval("{'name': '" + str(advertiser.name) +
                                             "', 'id': '" + str(advertiser.id) +
                                             "', 'version': '" + str(advertiser.version) +
                                             "', '_type': '" + str(advertiser._type) +
                                             "', 'agency_id': '" + str(advertiser.agency_id) +
                                             "', 'vertical_id ': '" + str(advertiser.vertical_id) +
                                             "', 'ad_server_id ': '" + str(advertiser.ad_server_id) +
                                             "', 'allow_x_strat_optimization ': '" + str(advertiser.allow_x_strat_optimization) +
                                             "', 'status ': '" + str(advertiser.status) +
                                             "', 'created_on ': '" + str(advertiser.created_on) +
                                             "', 'updated_on ': '" + str(advertiser.updated_on) +
                                             "', 'domain ': '" + str(advertiser.domain) +
                                             "', 'minimize_multi_ads ': '" + str(advertiser.minimize_multi_ads) +
                                             "', 'frequency_type': '" + str(advertiser.frequency_type) +
                                             "', 'frequency_interval ': '" + str(advertiser.frequency_interval) +
                                             "', 'dmp_enabled ': '" + str(advertiser.dmp_enabled) +
                                             "', 'data_sharing_enabled ': '" + str(advertiser.data_sharing_enabled) + "'}"))
            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        try:
            name = request.data.get('name')
            agency_id = request.data.get('agency')
            ad_server_id = request.data.get('adserver')
            domain = request.data.get('domain')
            vertical_id = request.data.get('vertical_id')
            status_request = obtain_status(request.data.get('status'))

            data_advertiser = {
                "name": name,
                "status": status_request,
                "agency_id": int(agency_id),
                "ad_server_id": int(ad_server_id),
                "domain": domain,
                "vertical_id": int(vertical_id),
            }
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            new_advertiser = connection.new("advertisers", properties=data_advertiser)
            new_advertiser.save()
            return Response({'Success': 'Advertiser creado con éxito'}, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def get_one_advertiser(request, pk):
    if request.method == 'GET':
        try:
            id_advertiser = pk
            response = []
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            advertiser = connection.get("advertisers", id_advertiser)

            response.append(literal_eval("{'name': '" + str(advertiser.name) +
                                         "', 'id': '" + str(advertiser.id) +
                                         "', 'version': '" + str(advertiser.version) +
                                         "', '_type': '" + str(advertiser._type) +
                                         "', 'agency_id': '" + str(advertiser.agency_id) +
                                         "', 'vertical_id ': '" + str(advertiser.vertical_id) +
                                         "', 'ad_server_id ': '" + str(advertiser.ad_server_id) +
                                         "', 'allow_x_strat_optimization ': '" + str(advertiser.allow_x_strat_optimization) +
                                         "', 'status ': '" + str(advertiser.status) +
                                         "', 'created_on ': '" + str(advertiser.created_on) +
                                         "', 'updated_on ': '" + str(advertiser.updated_on) +
                                         "', 'domain ': '" + str(advertiser.domain) +
                                         "', 'minimize_multi_ads ': '" + str(advertiser.minimize_multi_ads) +
                                         "', 'frequency_type': '" + str(advertiser.frequency_type) +
                                         "', 'frequency_interval ': '" + str(advertiser.frequency_interval) +
                                         "', 'dmp_enabled ': '" + str(advertiser.dmp_enabled) +
                                         "', 'data_sharing_enabled ': '" + str(advertiser.data_sharing_enabled) + "'}"))
            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            id_advertiser = pk
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            advertiser = connection.get("advertisers", id_advertiser)
            if request.data.get('name').strip():
                advertiser.name = str(request.data.get('name'))

            if request.data.get('typed').strip():
                advertiser._type = str(request.data.get('type'))

            if request.data.get('agency_id').strip():
                advertiser.agency_id = int(request.data.get('agency_id'))

            if request.data.get('vertical_id').strip():
                advertiser.vertical_id = int(request.data.get('vertical_id'))

            if request.data.get('ad_server_id').strip():
                advertiser.ad_server_id = int(request.data.get('ad_server_id'))

            if request.data.get('status').strip():
                advertiser.status = obtain_status(request.data.get('status'))


            if request.data.get('domain').strip():
                advertiser.domain = str(request.data.get('domain'))

            advertiser.save()

            return Response({'Success': 'Advertiser Actualizado con éxito'}, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)


