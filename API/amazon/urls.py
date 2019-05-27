from django.conf.urls import url
from . import views
from .views import amazon

urlpatterns = [
    url(
        r'scraper/',
        amazon.test_amazon,
        name='test_amazon'
    )
]