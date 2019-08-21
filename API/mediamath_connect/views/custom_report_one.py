import os
import gspread
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..connection import credentials as credential
from ..connection.mediamath_connection import MediaMathConnection
from oauth2client.service_account import ServiceAccountCredentials
from django.http import HttpResponse


def remove_all_whitespaces(sentence):
    return ''.join(sentence.split())


def remove_all_whitespaces_and_split(sentence, delimiter):
    return remove_all_whitespaces(sentence).split(delimiter)


@api_view(['POST'])
def get_report(request):
    try:
        # Data
        advertiser_id = remove_all_whitespaces(request.data.get('advertiser_id'))
        start_date = remove_all_whitespaces(request.data.get('start_date'))
        end_date = remove_all_whitespaces(request.data.get('end_date'))
        order = remove_all_whitespaces(request.data.get('order'))
        time_rollup = remove_all_whitespaces(request.data.get('time_rollup'))
        dimensions = remove_all_whitespaces_and_split(request.data.get('dimensions'), ',')
        metrics = remove_all_whitespaces_and_split(request.data.get('metrics'), ',')
        type_response = remove_all_whitespaces(request.data.get('type_response'))
        delimiter = ";"
        # Request
        connection = MediaMathConnection(credential.username, credential.password).connect()
        rpts = connection.new("report")
        report = connection.new("report", rpts.report_uri("performance"))
        report.set({'dimensions': dimensions,
                    'filter': {'advertiser_id': advertiser_id},
                    'metrics': metrics,
                    'time_rollup': time_rollup,
                    'start_date': start_date,
                    'end_date': end_date,
                    'order': [order]})
        # Get Response
        headers, data = report.get()
        csv_string = ''
        csv_string += delimiter.join(headers) + '\n'
        for row in data:
            for column in row:
                if re.match("^\d+?\.\d+?$", column) is None:
                    # String
                    csv_string += column + delimiter
                else:
                    colum_temp = round(float(column), 4)
                    decimals = str(colum_temp % 1).replace("0.", "")
                    if len(decimals) == 1 and decimals == "0":
                        # Integer
                        csv_string += str(int(colum_temp)) + delimiter
                    else:
                        # Float
                        csv_string += str(colum_temp).replace(".", ",") + delimiter
            csv_string += "\n"
            # csv_string += csv_temp[:len(csv_temp)-1] + "\n"
        # Set Responses
        if type_response == 'json':
            return Response({'Response': 'Json'}, status.HTTP_200_OK)
        elif type_response == 'csv':
            response = HttpResponse(csv_string, content_type='text/csv')
            return response
        elif type_response == 'google_sheets':
            spreed_shet_key = remove_all_whitespaces(request.data.get('spreed_shet_key'))
            work_sheet_name = remove_all_whitespaces(request.data.get('work_sheet_name'))
            system_file_location = os.path.dirname(__file__).replace('/views', '')
            credentials = ServiceAccountCredentials.from_json_keyfile_name(system_file_location +
                                                                           credential.key_file_location,
                                                                           credential.scopes)
            client = gspread.authorize(credentials)
            spread_sheet = client.open_by_key(spreed_shet_key)
            body = {
                'requests':
                [
                    {
                        'pasteData': {
                            "coordinate": {
                                "sheetId": str(spread_sheet.worksheet(work_sheet_name).id),
                                "rowIndex": "0",
                                "columnIndex": "0",
                            },
                            "data": csv_string,
                            "type": "PASTE_VALUES",
                            "delimiter": delimiter,
                        }
                    }
                ]
            }
            spread_sheet.batch_update(body)
            return Response({'Response': 'Success Google Sheets Upload'}, status.HTTP_200_OK)
        else:
            return Response({'Response': 'Enter a valid [type_response]'}, status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)
