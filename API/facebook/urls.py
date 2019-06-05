# FACEBOOK
from django.conf.urls import url
from .views import get_posts_comments, get_posts

urlpatterns = [
    url(
        r'comments/',
        get_posts_comments.get_posts_comments,
        name='get_posts_comments'
    ),
    url(
        r'posts/',
        get_posts.get_posts,
        name='get_posts'
    )
]