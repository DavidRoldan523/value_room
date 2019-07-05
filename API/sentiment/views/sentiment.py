import requests as requests_python
import csv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date as python_date
from dateutil.rrule import rrule, DAILY
from classifier import *
import re
from stop_words import get_stop_words


def get_requests(request):
    data = {}
    for key, value in request:
        data[key] = str(value).strip()
    return data


def get_reviews(data, token_api):
    if data['source'] == 'youtube':
        url = '/http://ec2-18-207-188-143.compute-1.amazonaws.com:8000/api/v1/youtube/videos/'
    elif data['source'] == 'facebook':
        url = 'http://ec2-18-207-188-143.compute-1.amazonaws.com:8000/api/v1/facebook/posts/'
    elif data['source'] == 'instagram':
        url = 'http://ec2-18-207-188-143.compute-1.amazonaws.com:8000/api/v1/instagram/posts/'
    else:
        return Response({'Response': 'This Source is not available'}, status.HTTP_400_BAD_REQUEST)
    header = {'Authorization': f'token {token_api}'}
    response = requests_python.post(url, data=data, headers=header)
    return response.json()


def transform_date(date):
    split_original_time = date.split('-')
    response = python_date(int(split_original_time[0]),
                           int(split_original_time[1]),
                           int(split_original_time[2]))
    return response


def clean_string(string):
    stop_words = get_stop_words('spanish')
    string = re.sub('[^\w]+', ' ', string.lower())
    string = re.sub(r"\b[a-zA-Z]{1}\b", '', string)
    string = re.sub("\d+", '', string)
    string = re.sub("\n", ' ', string)

    for word in stop_words:
        if re.findall(fr'\b({word})\b', string):
            string = re.sub(fr"\b({word})\b", '', string)
    return string


def get_frequency_words(string):
    string = clean_string(string)
    words_list = string.split()
    words_frequency = [words_list.count(word) for word in words_list]
    response = sorted(set(zip(words_list, words_frequency)), key=lambda x: x[1], reverse=True)
    return response


@api_view(['POST'])
def sentiment(request):
    try:
        token_api = str(request.META['HTTP_AUTHORIZATION']).split(' ')[1]
        data = get_requests(request.data.items())
        data_crude = get_reviews(data, token_api)[0]
        since = transform_date(data_crude['since'])
        until = transform_date(data_crude['until'])

        clf = SentimentClassifier()
        JSON_EXIT = [
            {
                'medium': '',
                'page_name': '',
                'page_id': '',
                'date_since': '',
                'date_until': '',
                'results': []
            }
        ]

        JSON_EXIT[0]['medium'] = data['source']
        JSON_EXIT[0]['page_name'] = data_crude['page_name']
        JSON_EXIT[0]['page_id'] = data_crude['page_id']
        JSON_EXIT[0]['date_since'] = data_crude['since']
        JSON_EXIT[0]['date_until'] = data_crude['until']

        for day in rrule(DAILY, dtstart=since, until=until):
            date_temp = day.strftime("%Y-%m-%d")
            result_total_temp = {
                'date': date_temp,
                'comments': [],
                'frequency_words': []
            }
            total_coments_by_day = ''
            for result in data_crude['results']:
                post_id = result['post_id']
                post_name = result['post_name']
                result_post_temp = {
                    'post_id': post_id,
                    'post_name': post_name,
                    'results': []
                }
                for comment in result['comments']:
                    if comment['created_time'] == date_temp:
                        comment_text = comment['comment_text']
                        polarity = clf.predict(comment_text)
                        comment_temp = {
                            'comment_text': comment_text,
                            'polarity': f'{polarity:.6f}'
                        }
                        result_post_temp['results'].append(comment_temp)
                        total_coments_by_day += comment_text

                if len(result_post_temp['results']) > 0:
                    result_total_temp['comments'].append(result_post_temp)

            if total_coments_by_day != '':
                for frecuency_words in get_frequency_words(clean_string(total_coments_by_day))[:50]:
                    frecuency_words_temp = {
                        'word': frecuency_words[0],
                        'frequency': frecuency_words[1]
                    }
                    result_total_temp['frequency_words'].append(frecuency_words_temp)

            if len(result_total_temp['comments']) > 0:
                JSON_EXIT[0]['results'].append(result_total_temp)

        return Response(JSON_EXIT, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': f'URL incorrecto: {e}'}, status.HTTP_400_BAD_REQUEST)


