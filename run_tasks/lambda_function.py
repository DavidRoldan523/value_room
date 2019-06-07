import concurrent.futures
from botocore.vendored import requests
from tools.dates import Date
from youtube import YouTube
from instagram import Instagram


def download_data(object_data):
    object_data.load_data()


def lambda_handler(event, context):
    try:
        list_objects = []
        dates = Date()
        post_instagram = Instagram(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/instagram/posts/',
                                   page_id='17841401363715944',
                                   token='e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                                   fb_token='EAAD3osazFggBAEmBWZCP72Tm1ZA6ZBsBRMqZC0pJ7mxUAU2UZASZA28VgLR7ZBQWXRlcjN5z8ZBGy27601K1VyJ0871ZC36lKV2K9qcLwZCaYZBwU1ei9daLbaC9gktq9X4M0Vz01CYDmEXdtO78RiVw1c43OKlc1JRWIVM4QUw0D6cZAgZDZD',
                                   database='dynamodb',
                                   database_table='post_instagram')
        videos = YouTube(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/youtube/videos/',
                         key='AIzaSyAvoNv_weASfNEeFQWFrhxQ32d14bd6zzQ',
                         channel_id='UCt1qSsMv-2RifMObrc0z52Q',
                         date=dates.date_youtube,
                         token='e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                         database='dynamodb',
                         database_table='videos')
        list_objects.append(videos)
        list_objects.append(post_instagram)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_data, list_objects)

        return {'Response': 'Success'}
    except Exception as e:
        return {'Response': f'Error: {e}'}
