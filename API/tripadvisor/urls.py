from django.conf.urls import url
from .views import tripadvisor

urlpatterns = [
    url(
        r'scraper/',
        tripadvisor.get_reviews,
        name='get_reviews'
    )
]