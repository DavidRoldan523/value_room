import concurrent.futures
from botocore.vendored import requests
from tools.date import Date
from youtube import YouTube
from instagram import Instagram
from facebook import Facebook
import random


def get_fb_token(data_fb_token):
    response = requests.post(data_fb_token['url'],
                             data={'previus_token': data_fb_token['previus_token']},
                             headers={'Authorization': f"Token {data_fb_token['token']}"})
    response = response.json()
    return response['Response']


def get_youtube_key():
    keys_list = ['AIzaSyCUuCL3fQYLe_4jb4axOA9fqg8Y7mpIHmM',
                 'AIzaSyCQQnZXr5ufAGSsSsob78Q2vyxrG1ANvps',
                 'AIzaSyCeQ3PkNB1HyJlb_AdYFOl4tUTy4_k2O5c',
                 'AIzaSyBlGtCmbR5inPwc9wJc2SQKxB9fpHoPFjg']
    return random.choice(keys_list)


def download_data(object_data):
    object_data.load_data()


def lambda_handler(event, context):
    try:
        common_data_services = {'token_api': 'e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                                'storage': {'name': 's3',
                                            'bucketfacebook': 'bucketfacebook',
                                            'bucketinstagram': 'bucketinstagram',
                                            'bucketyoutube': 'bucketytube'}}
        data_fb_token = {'url': 'http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/facebook/token/',
                         'previus_token': 'EAAD3osazFggBAO3y3V6olXlnM1yLeGQa6hWE2TEmH9XIM92pg4g6Ee6CZBf094sw1HHZCAK73cZC03pzxIrZACFr1FtzBbA0dSmRGMACzbEY23otq7upXWXPYubU3wLGLho3jGIKIcOe356dZCaWtkf2SZCicRx8YQiQILlh2COQZDZD',
                         'token': common_data_services['token_api']}
        fb_token = get_fb_token(data_fb_token)
        youtube_key = get_youtube_key()
        dates = Date()
        post_facebook = Facebook(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/facebook/posts/',
                                 page_id='113387205347979',
                                 token=common_data_services['token_api'],
                                 fb_token=fb_token,
                                 since=dates.dates_facebook['since'],
                                 until=dates.dates_facebook['until'],
                                 storage=common_data_services['storage']['name'],
                                 bucket=common_data_services['storage']['bucketfacebook'])
        post_instagram = Instagram(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/instagram/posts/',
                                   page_id='17841401363715944',
                                   token=common_data_services['token_api'],
                                   fb_token=fb_token,
                                   storage=common_data_services['storage']['name'],
                                   bucket=common_data_services['storage']['bucketinstagram'])
        videos = YouTube(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/youtube/videos/',
                         key=youtube_key,
                         channel_id='UCt1qSsMv-2RifMObrc0z52Q',
                         date=dates.date_youtube,
                         token=common_data_services['token_api'],
                         storage=common_data_services['storage']['name'],
                         bucket=common_data_services['storage']['bucketyoutube'])

        # Pila Excecution
        list_objects_threading = []
        list_objects_threading.append(post_facebook)
        list_objects_threading.append(post_instagram)
        list_objects_threading.append(videos)

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(download_data, list_objects_threading)

        return {'Response': 'Success'}
    except Exception as e:
        return {'Response': f'Error: {e}'}

