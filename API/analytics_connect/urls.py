from django.conf.urls import url
from .views import dimensions_and_metrics


urlpatterns = [
    url(
        r'dimensions_and_metrics/',
        dimensions_and_metrics.get_dimensions_and_metrics,
        name='get_dimensions_and_metrics'
    )
]
