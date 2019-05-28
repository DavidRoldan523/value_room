from django.conf.urls import url
from .views import youtube

urlpatterns = [
    url(
        r'video/',
        youtube.get_reviews_video,
        name='get_reviews_video'
    )
]