# SENTIMENT
from django.conf.urls import url
from .views import sentiment

urlpatterns = [
    url(
        r'',
        sentiment.sentiment,
        name='sentiment'
    )
]