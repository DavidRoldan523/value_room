import boto3
from botocore.vendored import requests
from tools.date import Date
import csv


def load_data(bucket, json):
    storage = 's3'
    file_name = json[0]["page_name"].replace(' ', '')
    with open(f"/tmp/{file_name}.csv", mode='w', newline='', encoding='utf8') as file:
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


def download_data(data):
    url = 'http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/sentiment/'
    headers = {'Authorization': "Token e91d9f6c9810bf07b419b2a141d6435d241c4e9f"}
    response = requests.post(url, data=data, headers=headers)
    load_data(data['bucket'], response.json())


def lambda_handler(event, context):
    try:
        dates = Date()
        facebook = {'page_id': '113387205347979',
                    'since': '2019-05-01',
                    'until': '2019-05-10',
                    'source': 'facebook',
                    'bucket': 'bucketfacebook'}

        instagram = {'page_id': '17841401363715944',
                     'source': 'instagram',
                     'bucket': 'bucketinstagram'}

        youtube = {'page_id': 'UCt1qSsMv-2RifMObrc0z52Q',
                   'date': dates.date_youtube,
                   'source': 'youtube',
                   'bucket': 'bucketytube'}

        download_data(youtube)
        download_data(instagram)
        download_data(facebook)

        return {'Response': 'Success'}
    except Exception as e:
        return {'Response': f'Error: {e}'}
