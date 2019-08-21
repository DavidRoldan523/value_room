from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
import urllib.parse
import json
from rest_framework import status

get_all_contacts_url = "https://api.hubapi.com/contacts/v1/lists/all/contacts/all?"
parameter_dict = {'hapikey': '6054df25-c3f0-429f-acbb-3366dda90c93', 'count': '300', 'vidOffset': ''}
contact_list = []
property_list = []
headers = {}


def remove_all_whitespaces(sentence):
    return ''.join(sentence.split())


def core_contacts_function(has_more):
    try:
        global get_all_contacts_url, parameter_dict, contact_list, property_list, headers
        parameters = urllib.parse.urlencode(parameter_dict)
        get_url = get_all_contacts_url + parameters
        r = requests_python.get(url=get_url, headers=headers)
        response_dict = json.loads(r.text)
        has_more = response_dict['has-more']
        contact_list.extend(response_dict['contacts'])
        parameter_dict['vidOffset'] = response_dict['vid-offset']
    except Exception as e:
        print(f'Error: {e}')
        core_contacts_function(has_more)
    return len(contact_list), parameter_dict['vidOffset']


@api_view(['POST'])
def get_contacts(request):
    # token = request.data.get('token')
    has_more = True
    count_temp = 0
    while (has_more):
        return_contact_list, return_vidoffset_capture = core_contacts_function(has_more)
        count_temp += 1
        print(f'{return_contact_list} + {return_vidoffset_capture} + {count_temp}')

    return Response({'Data': '500'}, status.HTTP_200_OK)
