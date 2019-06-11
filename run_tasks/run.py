import concurrent.futures
from botocore.vendored import requests
from tools.date import Date
from youtube import YouTube
from instagram import Instagram
from facebook import Facebook


def download_data(object_data):
    object_data.load_data()


def lambda_handler(event, context, fb_token):
    try:

        list_objects = []
        dates = Date()
        fb_token = 'EAAD3osazFggBAEmBWZCP72Tm1ZA6ZBsBRMqZC0pJ7mxUAU2UZASZA28VgLR7ZBQWXRlcjN5z8ZBGy27601K1VyJ0871ZC36lKV2K9qcLwZCaYZBwU1ei9daLbaC9gktq9X4M0Vz01CYDmEXdtO78RiVw1c43OKlc1JRWIVM4QUw0D6cZAgZDZD'
        youtube_key = 'AIzaSyAgsQk6Auw8miRqu_hzeDUu01YsGEts7-8'
        post_facebook = Facebook(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/facebook/posts/',
                                 page_id='113387205347979',
                                 token='e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                                 fb_token=fb_token,
                                 since=dates.dates_facebook['since'],
                                 until=dates.dates_facebook['until'],
                                 storage='s3',
                                 bucket='bucketfacebook')

        post_instagram = Instagram(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/instagram/posts/',
                                   page_id='17841401363715944',
                                   token='e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                                   fb_token=fb_token,
                                   storage='s3',
                                   bucket='bucketinstagram')

        videos = YouTube(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/youtube/videos/',
                         key=youtube_key,
                         channel_id='UCt1qSsMv-2RifMObrc0z52Q',
                         date=dates.date_youtube,
                         token='e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                         storage='s3',
                         bucket='bucketytube')

        # Pila Excecution
        list_objects.append(post_facebook)
        list_objects.append(post_instagram)
        list_objects.append(videos)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_data, list_objects)

        return {'Response': 'Success'}
    except Exception as e:
        return {'Response': f'Error: {e}'}

