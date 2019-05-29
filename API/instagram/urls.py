from django.conf.urls import url
from .views import instagram

urlpatterns = [
    url(
        r'posts/',
        instagram.get_comments,
        name='get_comments'
    ),
    url(
        r'accounts/',
        instagram.get_accounts_id,
        name='get_accounts_id'
    )
]