import os
import ast
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..connection import credentials as credential
from ..connection.googleAnalytics_connection import GoogleAnalyticsConnect
from django.http import HttpResponse


def remove_all_whitespaces(sentence):
    return ''.join(sentence.split())


def remove_all_whitespaces_and_split(sentence, delimiter):
    return remove_all_whitespaces(sentence).split(delimiter)


def get_request(request):
    data = {}
    delimiter = ','
    for key, value in request:
        if delimiter in value:
            # Is a List
            if key == 'dateRanges':
                date_ranges = remove_all_whitespaces_and_split(value, delimiter)
                if len(date_ranges) == 2:
                    # Only one range dates
                    date_temp = {}
                    date_temp['startDate'] = date_ranges[0]
                    date_temp['endDate'] = date_ranges[1]
                    data['dateRanges'] = ast.literal_eval(f"[{date_temp}]")
                else:
                    # Two range dates
                    date_temp1 = {}
                    date_temp1['startDate'] = date_ranges[0]
                    date_temp1['endDate'] = date_ranges[1]
                    date_temp2 = {}
                    date_temp2['startDate'] = date_ranges[2]
                    date_temp2['endDate'] = date_ranges[3]
                    data['dateRanges'] = ast.literal_eval(f"[{date_temp1},{date_temp2}]")

            elif key == 'metrics':
                metrics = remove_all_whitespaces_and_split(value, delimiter)
                metrics_temp = []
                for metric in metrics:
                    metrics_temp += {'expression': 'ga:' + metric},
                data[key] = metrics_temp

            elif key == 'dimensions':
                dimensions = remove_all_whitespaces_and_split(value, delimiter)
                dimensions_temp = []
                for dimension in dimensions:
                    dimensions_temp += {'name': 'ga:' + dimension},
                data[key] = dimensions_temp
            else:
                data[key] = remove_all_whitespaces_and_split(value, delimiter)
        elif key != "type_response":
            # Is only one String
            data[key] = remove_all_whitespaces(value)
    return data


@api_view(['POST'])
def get_dimensions_and_metrics(request):
    try:
        # Data
        data = get_request(request.data.items())
        type_response = remove_all_whitespaces(request.data.get("type_response"))
        # Request
        system_file_location = os.path.dirname(__file__).replace('/views', '')
        connection = GoogleAnalyticsConnect(system_file_location +
                                            credential.key_file_location,
                                            credential.scopes).connect()
        # Get Response
        response = connection.reports().batchGet(body={'reportRequests': [data]}).execute()
        # Set Response
        if type_response == 'json':
            return Response(response, status.HTTP_200_OK)
        elif type_response == 'csv':
            delimiter = ';'
            # Header
            csv_final = ''
            csv_final = delimiter.join(response['reports'][0]['columnHeader']['dimensions']).replace('ga:', '')
            for metric in response['reports'][0]['columnHeader']['metricHeader']['metricHeaderEntries']:
                csv_final += delimiter + metric['name'].replace('ga:', '')
            csv_final += '\n'
            # Body
            for row in response['reports'][0]['data']['rows']:
                csv_final += delimiter.join(row['dimensions'])
                csv_final += delimiter.join(row['metrics'][0]['values'])
                csv_final += '\n'
            response = HttpResponse(csv_final, content_type='text/csv')
            return response
        elif type_response == 'google_sheets':
            return Response({'Response': 'Success Google Sheets Upload'}, status.HTTP_200_OK)
        else:
            return Response({'Response': 'Enter a valid [type_response]'}, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)
