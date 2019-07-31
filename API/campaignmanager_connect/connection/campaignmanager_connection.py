
import googleapiclient.discovery
from google.oauth2 import service_account


class CampaignManagerConnect:
    def __init__(self, key_file_location, scopes):
        self.key_file_location = key_file_location
        self.scopes = scopes

    def connect(self):
        credentials = service_account.Credentials.from_service_account_file(self.key_file_location, scopes=self.scopes)
        dcm = googleapiclient.discovery.build('dfareporting', 'v3.3', credentials=credentials)
        return dcm
