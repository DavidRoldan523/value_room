from django.conf.urls import url
from .views import youtube_video, youtube_channel

urlpatterns = [
    url(
        r'video/',
        youtube_video.get_reviews_video,
        name='get_reviews_video'
    ),
    url(
        r'channel/',
        youtube_channel.get_reviews_all_videos,
        name='get_reviews_all_videos'
    )
]