from django.conf.urls import url
from .views import instagram

urlpatterns = [
    url(
        r'posts/',
        instagram.get_comments,
        name='get_comments'
    )
]