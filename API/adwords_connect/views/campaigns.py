from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..connection.adwords_connection import AdwordsConnect


def remove_all_whitespaces(sentence):
    return ''.join(sentence.split())


@api_view(['POST'])
def get_campaigns(request):
    try:
        # profile_id = remove_all_whitespaces(request.data.get('profile_id'))
        connection = AdwordsConnect().connect()
        # Construct selector and get all campaigns.
        offset = 0
        PAGE_SIZE = 100
        selector = {
            'fields': ['Id', 'Name', 'Status'],
            'paging': {
                'startIndex': str(offset),
                'numberResults': str(PAGE_SIZE)
            }
        }

        more_pages = True
        while more_pages:
            page = connection.get(selector)
            # Display results.
            if 'entries' in page:
                for campaign in page['entries']:
                    print(f"Campaign with id: {campaign['id']}, name: {campaign['name']},"
                          f"status: {campaign['status']}'")
            else:
                print('No campaigns were found.')
            offset += PAGE_SIZE
            selector['paging']['startIndex'] = str(offset)
            more_pages = offset < int(page['totalNumEntries'])

        return Response({'h': 'h'}, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)
