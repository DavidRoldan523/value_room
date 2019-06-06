from django.conf.urls import url
from .views import get_videos_comments, get_videos, get_videos_embedded

urlpatterns = [
    url(
        r'videos/embedded/',
        get_videos_embedded.get_videos_embedded,
        name='get_videos_embedded'
    )
]
"""
    url(
        r'videos/comments/',
        get_videos_comments.get_videos_comments,
        name='get_videos_comments'
    ),
    url(
        r'videos/',
        get_videos.get_videos,
        name='get_videos'
    ),
"""

