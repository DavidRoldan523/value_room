from YouTube import YouTube


def lambda_handler(event, context):
    videos = YouTube(url='http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/youtube/videos/',
                     key='AIzaSyAvoNv_weASfNEeFQWFrhxQ32d14bd6zzQ',
                     channel_id='UCt1qSsMv-2RifMObrc0z52Q',
                     date='2019-01-01T00:00:00-08:00',
                     token='e91d9f6c9810bf07b419b2a141d6435d241c4e9f',
                     database='dynamodb',
                     database_table='videos')
    videos.load_data()
    return {'h': 'h'}

