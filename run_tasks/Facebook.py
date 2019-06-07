from botocore.vendored import requests
import boto3

class Facebook:

    def __init__(self, url, page_id, token, fb_token, since, until, database, database_table):
        self.url = url
        self.page_id = page_id
        self.token = token
        self.fb_token = fb_token
        self.since = since
        self.until = until
        self.database = database
        self.database_table = database_table

    def get_data(self):
        response = requests.post(f'{self.url}',
                                 data={'page_id': f'{self.page_id}',
                                       'token': f'{self.fb_token}',
                                       'since': f'{self.since}',
                                       'until': f'{self.until}'},
                                 headers={'Authorization': f'Token {self.token}'})
        return response.json()

        
    def load_data(self):
        database = boto3.resource(self.database)
        table = database.Table(self.database_table)
        for post in self.get_data():
            table.put_item(Item=post)
