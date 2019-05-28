from django.conf.urls import url
from .views import instagram

urlpatterns = [
    url(
        r'posts/',
        instagram.get_posts_id,
        name='get_posts_id'
    )
]