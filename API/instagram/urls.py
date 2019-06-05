from django.conf.urls import url
from .views import get_comments, get_posts

urlpatterns = [
    url(
        r'posts/',
        get_posts.get_posts,
        name='get_posts'
    ),
    url(
        r'comments/',
        get_comments.get_comments,
        name='get_comments'
    )
]