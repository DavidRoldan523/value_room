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

    def get_data(self):
        response = requests.post(f'{self.url}',
                                 data={'key': f'{self.key}',
                                       'channel_id': f'{self.channel_id}',
                                       'date': f'{self.date}'},
                                 headers={'Authorization': f'Token {self.token}'})
        return response.json()

    def load_data(self):
        database = boto3.resource(self.database)
        table = database.Table(self.database_table)
        # Clear previous Data
        scan = table.scan()
        with table.batch_writer() as batch:
            for item in scan['Items']:
                if item['video_id'] != '1':
                    batch.delete_item(Key={'video_id': item['video_id']})
        for video in self.get_data():
            table.put_item(Item=video)
