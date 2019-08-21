
from django.conf.urls import url
from .views import advertiser
from .views import adserver
from .views import agencie
from .views import campaign
from .views import videocreative
from .views import report
from .views import custom_report_one
from .views import token


app_name = 'mediamath_connect'

urlpatterns = [
    # ADSERVERS
    url(r'adservers/$', adserver.get_adservers, name='get_adservers'),
    url(r'adservers/(?P<pk>[0-9]+)$', adserver.get_one_adserver, name='get_one_adserver'),

    # ADVERTISERS
    url(r'advertisers/(?P<pk>[0-9]+)$', advertiser.get_one_advertiser, name='get_one_advertiser'),
    url(r'advertisers/', advertiser.get_advertisers, name='get_advertisers'),

    # AGENCIES
    url(r'agencies/(?P<pk>[0-9]+)$', agencie.get_one_agencie, name='get_one_agencie'),
    url(r'agencies/', agencie.get_agencies, name='get_agencies'),

    # CAMPAIGNS
    url(r'campaigns/(?P<pk>[0-9]+)$', campaign.get_one_campaign, name='get_one_camapaign'),
    url(r'campaigns/', campaign.get_campaigns, name='get_camapaigns'),

    # VIDEO CREATIVES
    url(r'videocreatives/(?P<pk>[0-9]+)$', videocreative.get_one_videocreative, name='get_one_videocreative'),
    url(r'videocreatives/', videocreative.get_videocreatives, name='get_videocreatives'),

    # REPORTS
    url(r'report/', report.get_report, name='get_report'),
    url(r'custom_report_one/', custom_report_one.get_report, name='custom_report_one'),

    # Token
    url(r'token/', token.get_token, name='get_token'),


]
