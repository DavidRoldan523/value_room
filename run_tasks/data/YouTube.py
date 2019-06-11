from botocore.vendored import requests
import boto3
import json


class YouTube:
    def __init__(self, url, key, channel_id, date, token, storage, bucket):
        self.url = url
        self.key = key
        self.channel_id = channel_id
        self.date = date
        self.token = token
        self.storage = storage
        self.bucket = bucket
        self.file_name = ''

    def get_data(self):
        response = requests.post(f'{self.url}',
                                 data={'key': f'{self.key}',
                                       'channel_id': f'{self.channel_id}',
                                       'date': f'{self.date}'},
                                 headers={'Authorization': f'Token {self.token}'})
        return response.json()

    def load_data(self):
        response = self.get_data()
        self.file_name = response[0]["channel_name"].replace(' ', '')
        with open(f"/tmp/{self.file_name}.json", "w") as file:
            json.dump(response, file)

        connection = boto3.client(self.storage)
        connection.upload_file(f"/tmp/{self.file_name}.json", self.bucket, f"{self.file_name}.json")

