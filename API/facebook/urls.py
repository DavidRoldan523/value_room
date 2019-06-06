# FACEBOOK
from django.conf.urls import url
from .views import get_posts_comments, get_posts, get_posts_embedded

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
    ),
    url(
        r'embedded/',
        get_posts_embedded.get_posts_embedded,
        name='get_post_embedded'
    )
]