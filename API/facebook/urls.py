from django.conf.urls import url
from .views import facebook

urlpatterns = [
    url(
        r'posts/',
        facebook.get_posts_id,
        name='get_posts_id'
    )
]