from django.conf.urls import url
from .views import audience

urlpatterns = [
    url(
        r'audience/',
        audience.get_audience,
        name='get_audience'
    )
] 