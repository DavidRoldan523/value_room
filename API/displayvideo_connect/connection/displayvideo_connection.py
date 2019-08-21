import os
import httplib2
from oauth2client import client
from oauth2client import file as oauthFile
from oauth2client import tools
from googleapiclient import discovery


class DisplayVideoConnect:
    def __init__(self, key_file_location, scopes):
        self.key_file_location = key_file_location
        self.scopes = scopes

    def load_application_default_credentials(self):
        try:
            credentials = client.GoogleCredentials.get_application_default()
            return credentials.create_scoped(self.scopes)
        except client.ApplicationDefaultCredentialsError:
            pass

    def load_user_credentials(self, client_secrets, storage):
        flow = client.flow_from_clientsecrets(client_secrets, scope=self.scopes)
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        return credentials

    def connect(self):
        credentials = self.load_application_default_credentials()
        if credentials is None:
            storage = oauthFile.Storage(os.path.join(os.path.dirname(__file__), 'doubleclickbidmanager.dat'))
            credentials = self.load_user_credentials(self.key_file_location, storage)
        http = credentials.authorize(http=httplib2.Http())
        displayvideo = discovery.build('doubleclickbidmanager', 'v1', http=http)
        return displayvideo
