from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views

urlpatterns = [
    #Apps
    url(r'^api/v1/amazon/', include('amazon.urls')),
    url(r'^api/v1/tripadvisor/', include('tripadvisor.urls')),
    url(r'^api/v1/facebook/', include('facebook.urls')),
    url(r'^api/v1/instagram/', include('instagram.urls')),
    url(r'^api/v1/youtube/', include('youtube.urls')),
    url(r'^api/v1/promodescuentos/', include('promodescuentos.urls')),
    url(r'^api/v1/sentiment/', include('sentiment.urls')),
    url(r'^api/v1/brandwatch/', include('brandwatch_connect.urls')),
    url(r'^api/v1/displayvideo/', include('displayvideo_connect.urls')),
    url(r'^api/v1/analytics/', include('analytics_connect.urls')),
    url(r'^api/v1/hubspot/', include('hubspot_connect.urls')),
    url(r'^api/v1/mediamath/', include('mediamath_connect.urls')),
    url(r'^api/v1/semrush/', include('semrush_connect.urls')),
    url(r'^api/v1/campaignmanager/', include('campaignmanager_connect.urls')),
    url(r'^api/v1/adwords/', include('adwords_connect.urls')),
    
    # Token
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
