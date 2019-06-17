from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status
from classifier import *

response_final = \
        {
            'medium': '',
            'comments': [],
            'frequency_words':
                [
                    {
                        'date': '',
                        'words':
                            [
                                {
                                    'word': '',
                                    'frequency': 0
                                }
                            ]
                    }
                ]
        }


def get_requests(request):
    data = {}
    for key, value in request:
        data[key] = str(value).strip()
    return data


def get_reviews(data, token_api):
    global response_final
    response_final['medium'] = ''
    if data['source'] == 'youtube':
        response_final['medium'] = 'youtube'
        url = 'http://localhost:8000/api/v1/youtube/videos/'
    elif data['source'] == 'facebook':
        response_final['medium'] = 'facebook'
        url = 'http://localhost:8000/api/v1/facebook/posts/'
    elif data['source'] == 'instagram':
        response_final['medium'] = 'instagram'
        url = 'http://localhost:8000/api/v1/instagram/posts/'
    else:
        return Response({'Response': 'This Source is not available'}, status.HTTP_400_BAD_REQUEST)
    del data['source']
    header = {'Authorization': f'token {token_api}'}
    response = requests_python.post(url, data=data, headers=header)
    return response.json()


def get_polarity(data):
    global response_final
    clf = SentimentClassifier()
    for post in data:
        for review in post['comments']:
            polarity = clf.predict(review['comment_text'])
            temp_dict = {
                            'comment_text': review['comment_text'],
                            'created_time': review['created_time'],
                            'polarity': polarity
                        }
            response_final['comments'].append(temp_dict)


def get_frequency_words(data):
    pass


@api_view(['POST'])
def sentiment(request):
    try:
        global response_final
        response_final['comments'].clear()
        token_api = str(request.META['HTTP_AUTHORIZATION']).split(' ')[1]
        data = get_requests(request.data.items())
        response = get_reviews(data, token_api)
        print(len(response_final['comments']))
        get_polarity(response)
        return Response({'h': 'h'}, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': f'URL incorrecto: {e}'}, status.HTTP_400_BAD_REQUEST)


