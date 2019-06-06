from django.conf.urls import url
from .views import get_comments, get_posts, get_posts_embedded

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
    ),
    url(
        r'posts/embedded',
        get_posts_embedded.get_comments,
        name='get_posts_embedded'
    )
]