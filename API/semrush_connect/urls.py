from django.conf.urls import url
from .views import get_url_keyword


urlpatterns = [
    url(
        r'keywords/',
        get_url_keyword.get_url_keyword,
        name='get_url_keyword'
    )
]