import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetConnection:
    def __init__(self, client_secret, scope):
        self.client_secret = client_secret
        self.scope = scope

    def connect(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.client_secret, self.scope)
        client = gspread.authorize(credentials)
        return client


