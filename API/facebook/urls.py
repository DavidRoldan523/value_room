from django.conf.urls import url
from .views import facebook

urlpatterns = [
    url(
        r'posts/',
        facebook.get_posts_id,
        name='get_posts_id'
    ),
    url(
        r'comments/',
        facebook.get_reviews_by_id_post,
        name='get_reviews_by_id_post'
    )
]