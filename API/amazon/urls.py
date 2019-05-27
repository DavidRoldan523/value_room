from django.conf.urls import url
from .views import amazon

urlpatterns = [
    url(
        r'scraper/',
        amazon.get_reviews,
        name='get_reviews'
    )
]