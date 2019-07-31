from django.conf.urls import url
from .views import campaigns


urlpatterns = [
    url(
        r'campaigns/',
        campaigns.get_campaigns,
        name='get_campaigns'
    )
]
