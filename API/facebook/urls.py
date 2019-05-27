from django.conf.urls import url
from .views import facebook

urlpatterns = [
    url(
        r'posts/',
        facebook.get_reviews_posts,
        name='get_reviews_posts'
    )
]