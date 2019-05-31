from django.conf.urls import url
from .views import youtube

urlpatterns = [
    url(
        r'videos/',
        youtube.get_reviews_videos,
        name='get_reviews_videos'
    )
]