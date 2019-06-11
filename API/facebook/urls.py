# FACEBOOK
from django.conf.urls import url
from .views import get_posts, get_token

urlpatterns = [
    url(
        r'posts/',
        get_posts.get_comments,
        name='get_comments'
    ),
    url(
        r'token/',
        get_token.get_token,
        name='get_token'
    )
]