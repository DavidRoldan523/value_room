from django.conf.urls import url
from .views import token


urlpatterns = [
    url(
        r'token/',
        token.get_token,
        name='get_token'
    )
]