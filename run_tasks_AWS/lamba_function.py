import concurrent.futures
import boto3
import threading
from botocore.vendored import requests
from tools.date import Date
import json
import csv

thread_local = threading.local()


def load_data_json(response):
    file_name = response[0]["channel_name"].replace(' ', '')
    with open(f"/tmp/{file_name}.json", "w") as file:
        json.dump(response, file)

    connection = boto3.client('s3')
    connection.upload_file(f"/tmp/{file_name}.json", 'bucketytube', f"{file_name}.json")


def load_data(bucket, json):
    storage = 's3'
    file_name = json[0]["page_name"].replace(' ', '')
    with open(f"/tmp/{file_name}.csv", mode='w', newline='', encoding='utf-8') as file:
        row_csv = csv.writer(file, delimiter=',')
        columns = ['medium', 'page_name', 'page_id', 'date_since',
                   'date_until', 'date', 'post_id', 'post_name',
                   'comment_text', 'polarity', 'word', 'frequency']
        row_csv.writerow(columns)
        for m in json:
            medium = m['medium']
            page_name = m['page_name']
            page_id = m['page_id']
            date_since = m['date_since']
            date_until = m['date_until']
            for results in json[0]['results']:
                date = results['date']
                for comment in results['comments']:
                    post_id = comment['post_id']
                    post_name = comment['post_name']
                    for post in comment['results']:
                        comment_text = post['comment_text']
                        polarity = post['polarity']
                        for frequency in results['frequency_words']:
                            word = frequency['word']
                            freq = frequency['frequency']
                            string = f"{medium}|{page_name}|{page_id}|{date_since}|{date_until}|" \
                                f"{date}|" \
                                f"{post_id}|{post_name}|{comment_text}|{polarity}|" \
                                f"{word}|{freq}"
                            response = string.split('|')
                            row_csv.writerow(response)

    connection = boto3.client(storage)
    connection.upload_file(f"/tmp/{file_name}.csv", bucket, f"{file_name}.csv")


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_data(data):
    session = get_session()
    url = 'http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/sentiment/'
    headers = {'Authorization': "Token e91d9f6c9810bf07b419b2a141d6435d241c4e9f"}
    with session.post(url, data=data, headers=headers) as response:
        response = response.json()
        load_data(data['bucket'], response)


def lambda_handler(event, context):
    try:
        dates = Date()
        facebook = {'page_id': '113387205347979',
                    'since': dates.dates_facebook['since'],
                    'until': dates.dates_facebook['until'],
                    'source': 'facebook',
                    'bucket': 'bucketfacebook'}

        instagram = {'page_id': '17841401363715944',
                     'source': 'instagram',
                     'bucket': 'bucketinstagram'}

        youtube = {'page_id': 'UCt1qSsMv-2RifMObrc0z52Q',
                   'date': dates.date_youtube,
                   'source': 'youtube',
                   'bucket': 'bucketytube'}

        # Pila Excecution
        list_objects_threading = []
        # list_objects_threading.append(facebook)
        list_objects_threading.append(instagram)
        list_objects_threading.append(youtube)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_data, list_objects_threading)

        return {'Response': 'Success'}
    except Exception as e:
        return {'Response': f'Error: {e}'}
