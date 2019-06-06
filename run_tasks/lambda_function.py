import json
import boto3
from botocore.vendored import requests


def lambda_handler(event, context):
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('test_python')
    table.put_item(
       Item={'id_test_python': '12312312',
             'username': 'janedoe',
             'first_name': 'Jane',
             'last_name': 'Doe',
             'age': 25,
             'account_type': 'standard_user'}
    )
    response = requests.post('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/facebook/posts/',
                              data={'page_id': '113387205347979',
                                    'token': 'EAAD3osazFggBALzDNZAONDR50uEzPJSGqrtZAu5ZBbzsLdWTtygePXncGps8rg1tuFD5i43h3E9H0VgaqP8r47hto7dZBkQt6s45QBKvIHSdP7tHxwyYeRZAeX3qZB7OC0HIIPbZAnbLgl9WqyrNJo8JEi3RZBZBfsp81lYRCkfOAZCuaeQ70JVlFZB3hkzoKXORWZCW6XCpL2MMBwZDZD',
                                    'fields': 'id,message,created_time',
                                    'since': '2019-05-20',
                                    'until': '2019-05-29'},
                              headers={'Authorization': 'Token e91d9f6c9810bf07b419b2a141d6435d241c4e9f '})
    """

    response_youtube_videos = requests.post('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/youtube/videos/',
                                              data={'key': 'AIzaSyAvoNv_weASfNEeFQWFrhxQ32d14bd6zzQ',
                                                    'channel_id': 'UCt1qSsMv-2RifMObrc0z52Q',
                                                    'date': '2019-01-01T00:00:00-08:00'},
                                              headers={'Authorization': 'Token e91d9f6c9810bf07b419b2a141d6435d241c4e9f '})
    return response_youtube_videos.json()
