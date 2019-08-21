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

def get_data_individual_campaign(campaign):
    return literal_eval("{'name': '" + str(campaign.name) +
                         "', 'id': '" + str(campaign.id) +
                         "', '_type': '" + str(campaign._type) +
                         # "', 'ad_server_fee': '" + campaign.ad_server_fee +
                         "', 'ad_server_id': '" + str(campaign.ad_server_id) +
                         "', 'agency_fee_pct': '" + str(campaign.agency_fee_pct) +
                         "', 'conversion_type': '" + str(campaign.conversion_type) +
                         "', 'conversion_variable_minutes': '" + str(campaign.conversion_variable_minutes) +
                         "', 'created_on': '" + str(campaign.created_on) +
                         "', 'currency_code': '" + str(campaign.currency_code) +
                         "', 'dcs_data_is_campaign_level': '" + str(campaign.dcs_data_is_campaign_level) +
                         "', 'end_date': '" + str(campaign.end_date) +
                         # "', 'entity_type': '" + str(campaign.entity_type) +
                         "', 'frequency_amount': '" + str(campaign.frequency_amount) +
                         "', 'frequency_interval': '" + str(campaign.frequency_interval) +
                         "', 'frequency_optimization': '" + str(campaign.frequency_optimization) +
                         "', 'frequency_type': '" + str(campaign.frequency_type) +
                         "', 'goal_type': '" + str(campaign.goal_type) +
                         "', 'goal_value': '" + str(campaign.goal_value) +
                         "', 'has_custom_attribution': '" + str(campaign.has_custom_attribution) +
                         # "', 'impression_cap_amount': '" + str(campaign.impression_cap_amount) +
                         "', 'impression_cap_automatic': '" + str(campaign.impression_cap_automatic) +
                         "', 'impression_cap_type': '" + str(campaign.impression_cap_type) +
                         "', 'initial_start_date': '" + str(campaign.initial_start_date) +
                         # "', 'io_name': '" + str(campaign.io_name) +
                         # "', 'io_reference_num': '" + str(campaign.io_reference_num) +
                         "', 'margin_pct': '" + str(campaign.margin_pct) +
                         # "', 'merit_pixel_id': '" + str(campaign.merit_pixel_id) +
                         "', 'minimize_multi_ads': '" + str(campaign.minimize_multi_ads) +
                         "', 'override_suspicious_traffic_filter': '" + str(campaign.override_suspicious_traffic_filter) +
                         # "', 'pc_window_minutes': '" + str(campaign.pc_window_minutes) +
                         "', 'pv_pct': '" + str(campaign.pv_pct) +
                         # "', 'pv_window_minutes': '" + str(campaign.pv_window_minutes) +
                         # "', 'restrict_targeting_to_deterministic_id': '" + str(campaign.restrict_targeting_to_deterministic_id) +
                         "', 'restrict_targeting_to_same_device_id': '" + str(campaign.restrict_targeting_to_same_device_id) +
                         "', 'service_type': '" + str(campaign.service_type) +
                         # "', 'spend_cap_amount': '" + str(campaign.spend_cap_amount) +
                         "', 'spend_cap_automatic': '" + str(campaign.spend_cap_automatic) +
                         "', 'spend_cap_type': '" + str(campaign.spend_cap_type) +
                         "', 'start_date': '" + str(campaign.start_date) +
                         "', 'status': '" + str(campaign.status) +
                         "', 'suspicious_traffic_filter_level': '" + str(campaign.suspicious_traffic_filter_level) +
                         "', 'total_budget': '" + str(campaign.total_budget) +
                         "', 'updated_on': '" + str(campaign.updated_on) +
                         "', 'use_default_ad_server': '" + str(campaign.use_default_ad_server) +
                         "', 'use_mm_freq': '" + str(campaign.use_mm_freq) +
                         "', 'version': '" + str(campaign.version) +
                         "', 'zone_name': '" + str(campaign.zone_name) + "'}")


@api_view(['GET', 'POST'])
def get_campaigns(request):
    if request.method == 'GET':
        try:
            connection = MediaMathConnection(credential.username, credential.password).connect()
            campaigns = connection.get("campaigns")
            response = []
            for individual_campaign in campaigns:
                campaign = connection.get("campaigns", individual_campaign.id)
                response.append(get_data_individual_campaign(campaign))
            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        try:
            organization_id = request.data.get('organization')
            status_request = obtain_status(request.data.get('status'))

            data_campaign = {
                "organization_id": int(organization_id),
                "status": status_request,
            }
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            new_campaign = connection.new("campaigns", properties=data_campaign)
            new_campaign.save()
            return Response({'Success': 'campaign creada con éxito'}, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_one_campaign(request, pk):
    if request.method == 'GET':
        try:
            id_campaign = pk
            response = []
            connection = MediaMathConnection(credential.username, credential.password).connect()
            campaign = connection.get("campaigns", id_campaign)
            response = get_data_individual_campaign(campaign)
            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        try:
            id_campaign = pk
            connection = MediaMathConnection(credential.username,
                                             credential.password).connect()
            campaign = connection.get("campaigns", id_campaign)

            if request.data.get('organization_id').strip():
                campaign.organization_id = int(request.data.get('organization_id'))

            if request.data.get('status').strip():
                campaign.status = obtain_status(request.data.get('status'))

            if request.data.get('version').strip():
                campaign.version = int(request.data.get('version'))

            campaign.save()

            return Response({'Success': 'campaign Actualizada con éxito'}, status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)
