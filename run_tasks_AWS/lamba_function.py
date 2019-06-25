from botocore.vendored import requests
from tools.date import Date
from tools.json_to_csv import JsonToCsv


def download_data(data):
    url = 'http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/sentiment/'
    headers = {'Authorization': "Token e91d9f6c9810bf07b419b2a141d6435d241c4e9f"}
    response = requests.post(url, data=data, headers=headers)
    JsonToCsv(data['bucket'], response.json(), 's3').load_data()


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

        download_data(youtube)
        download_data(instagram)
        download_data(facebook)

        return {'Response': 'Success'}
    except Exception as e:
        return {'Response': f'Error: {e}'}
