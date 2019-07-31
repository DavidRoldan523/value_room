from django.conf.urls import url
from .views import displayandvideo, get_list_queries, get_query, delete_query


urlpatterns = [
    url(
        r'reports/',
        displayandvideo.get_report,
        name='get_report'
    ),
    url(
        r'queries/',
        get_list_queries.get_list_queries,
        name='get_list_queries'
    ),
    url(
        r'query/',
        get_query.get_query,
        name='get_query'
    ),
    url(
        r'deletequery/',
        delete_query.delete_query,
        name='delete_query'
    )
]
