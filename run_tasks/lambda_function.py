from YouTube import YouTube
from Facebook import Facebook
from Instagram import Instagram


def lambda_handler(event, context):
    videos = YouTube(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/youtube/videos/',
                     key='AIzaSyAvoNv_weASfNEeFQWFrhxQ32d14bd6zzQ',
                     channel_id='UCt1qSsMv-2RifMObrc0z52Q',
                     date='2019-01-01T00:00:00-08:00',
                     token='e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                     database='dynamodb',
                     database_table='videos')
    videos.load_data()

    post_facebook = Facebook(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/facebook/posts/',
                     page_id='113387205347979',
                     token='e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                     fb_token='EAAD3osazFggBAEmBWZCP72Tm1ZA6ZBsBRMqZC0pJ7mxUAU2UZASZA28VgLR7ZBQWXRlcjN5z8ZBGy27601K1VyJ0871ZC36lKV2K9qcLwZCaYZBwU1ei9daLbaC9gktq9X4M0Vz01CYDmEXdtO78RiVw1c43OKlc1JRWIVM4QUw0D6cZAgZDZD',
                     since ='2019-05-01',
                     until ='2019-05-29',
                     database='dynamodb',
                     database_table='post_facebook')
    post_facebook.load_data()

    post_instagram = Instagram(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/instagram/posts/',
                     page_id='17841401363715944',
                     token='e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                     fb_token='EAAD3osazFggBAEmBWZCP72Tm1ZA6ZBsBRMqZC0pJ7mxUAU2UZASZA28VgLR7ZBQWXRlcjN5z8ZBGy27601K1VyJ0871ZC36lKV2K9qcLwZCaYZBwU1ei9daLbaC9gktq9X4M0Vz01CYDmEXdtO78RiVw1c43OKlc1JRWIVM4QUw0D6cZAgZDZD',
                     database='dynamodb',
                     database_table='post_instagram')
    post_instagram.load_data()

    return {'h': 'h'}

