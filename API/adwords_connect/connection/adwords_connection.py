import os
from googleads import adwords


class AdwordsConnect:
    def connect(self):
        credentials = adwords.AdWordsClient.LoadFromStorage(os.path.join(os.path.dirname(__file__), 'google_ads.yml'))
        adwords_client = credentials.GetService('CampaignService', version='v201809')
        return adwords_client
