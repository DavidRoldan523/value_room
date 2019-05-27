from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views

urlpatterns = [
    #Apps
    url(r'^api/v1/amazon/', include('amazon.urls')),
    
    # Token
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
