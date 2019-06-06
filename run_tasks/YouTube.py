from botocore.vendored import requests
import boto3

class YouTube:

    def __init__(self, url, key, channel_id, date, token, database, database_table):
        self.url = url
        self.key = key
        self.channel_id = channel_id
        self.date = date
        self.token = token
        self.database = database
        self.database_table = database_table

    def load_data(self):
        response = requests.post(f'{self.url}',
                                 data={'key': f'{self.key}',
                                       'channel_id': f'{self.channel_id}',
                                       'date': f'{self.date}'},
                                 headers={'Authorization': f'Token {self.token}'})
        database = boto3.resource(self.database)
        table = database.Table(self.database_table)
        for video in response.json():
            table.put_item(Item=video)
