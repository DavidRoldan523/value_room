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
def get_agencies(request):
    if request.method == 'GET':
        try:
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            agencies = connection.get("agencies")
            response = []

            for agencie_one in agencies:
                agencie = connection.get("agencies", agencie_one.id)
                response.append(literal_eval("{'name': '" + str(agencie.name) +
                                             "', 'id': '" + str(agencie.id) +
                                             "', 'version': '" + str(agencie.version) +
                                             "', '_type': '" + str(agencie._type) +
                                             "', 'organization_id': '" + str(agencie.organization_id) +
                                             "', 'created_on ': '" + str(agencie.created_on) +
                                             "', 'updated_on ': '" + str(agencie.updated_on) +
                                             "', 'status ': '" + str(agencie.status) +
                                             "', 'allow_x_adv_pixels ': '" + str(agencie.allow_x_adv_pixels) +
                                             "', 'allow_x_adv_optimization ': '" + str(agencie.allow_x_adv_pixels) +
                                             "', 'dmp_enabled ': '" + str(agencie.dmp_enabled) +
                                             "', 'eligible_for_data_sharing ': '" + str(agencie.eligible_for_data_sharing) + "'}"))

            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        try:
            organization_id = request.data.get('organization')
            status_request = obtain_status(request.data.get('status'))

            data_agencie = {
                "organization_id": int(organization_id),
                "status": status_request,
            }
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            new_agencie = connection.new("agencies", properties=data_agencie)
            new_agencie.save()
            return Response({'Success': 'Agencie creada con éxito'}, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_one_agencie(request, pk):
    if request.method == 'GET':
        try:
            id_agencie = pk
            response = []
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            agencie = connection.get("agencies", id_agencie)
            response.append(literal_eval("{'name': '" + str(agencie.name) +
                                         "', 'id': '" + str(agencie.id) +
                                         "', 'version': '" + str(agencie.version) +
                                         "', '_type': '" + str(agencie._type) +
                                         "', 'organization_id': '" + str(agencie.organization_id) +
                                         "', 'created_on ': '" + str(agencie.created_on) +
                                         "', 'updated_on ': '" + str(agencie.updated_on) +
                                         "', 'status ': '" + str(agencie.status) +
                                         "', 'allow_x_adv_pixels ': '" + str(agencie.allow_x_adv_pixels) +
                                         "', 'allow_x_adv_optimization ': '" + str(agencie.allow_x_adv_pixels) +
                                         "', 'dmp_enabled ': '" + str(agencie.dmp_enabled) +
                                         "', 'eligible_for_data_sharing ': '" + str(agencie.eligible_for_data_sharing) + "'}"))
            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        try:
            id_agencie = pk
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            agencie = connection.get("agencies", id_agencie)

            if request.data.get('organization_id').strip():
                agencie.organization_id = int(request.data.get('organization_id'))

            if request.data.get('status').strip():
                agencie.status = obtain_status(request.data.get('status'))

            if request.data.get('version').strip():
                agencie.version = int(request.data.get('version'))

            agencie.save()

            return Response({'Success': 'Agencie Actualizada con éxito'}, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)
