from django.conf.urls import url
from .views import promodescuentos

urlpatterns = [
    url(
        r'quiz/',
        promodescuentos.get_reviews,
        name='get_reviews'
    ),
]