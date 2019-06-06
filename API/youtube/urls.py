from django.conf.urls import url
from .views import get_videos

urlpatterns = [
    url(
        r'videos/',
        get_videos.get_videos,
        name='get_videos'
    )
]


