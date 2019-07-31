import json as json_python
import csv
import numpy as np
from ast import literal_eval
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..connection import credentials as credential
from ..connection.mediamath_connection import MediaMathConnection


def parse_list_to_csv(name, list):
    temp = list
    with open(f"{name}.csv", mode='w', newline='') as file:
        employee_writer = csv.writer(file, delimiter=',')
        employee_writer.writerow(temp[0])
        for row in temp[1]:
            employee_writer.writerow(row)


def get_filters(filters):
    response = {}
    for filter in filters:
        temp = filter.split('=')
        response = {temp[0]: temp[1]}
    return response


def get_request(request):
    data = {}
    for key, value in request:
        if key in ('time_rollup', 'start_date', 'end_date', 'type', 'file_name', 'format_file_exit'):
            data[key] = value
        elif key == 'filter':
            data[key] = get_filters(value.split(','))
        else:
            data[key] = value.split(',')
    return data



@api_view(['POST'])
def get_report(request):
    try:
        data = get_request(request.data.items())
        connection = MediaMathConnection(credential.username,
                                         credential.password).connect()
        report = connection.new("report", connection.new("report").report_uri(data['type']))
        report.set(data)
        response = report.get()

        if data['format_file_exit'] == 'csv':
            parse_list_to_csv(data['file_name'], response)
            return Response({'response': 'Download this file in Root Directory'}, status.HTTP_200_OK)
        else:
            return Response(response, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': str(e)}, status.HTTP_400_BAD_REQUEST)

