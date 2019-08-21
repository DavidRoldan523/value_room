from django.conf.urls import url
from .views import contacts


urlpatterns = [
    url(
        r'contacts/',
        contacts.get_contacts,
        name='get_contacts'
    ),
]
