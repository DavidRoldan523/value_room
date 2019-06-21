# FACEBOOK
from django.conf.urls import url
from .views import get_posts

urlpatterns = [
    url(
        r'posts/',
        get_posts.get_comments,
        name='get_comments'
    ),
]