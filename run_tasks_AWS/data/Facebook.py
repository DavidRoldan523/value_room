from botocore.vendored import requests
import boto3
import json


class Facebook:

    def __init__(self, url, page_id, token, fb_token, since, until, storage, bucket):
        self.url = url
        self.page_id = page_id
        self.token = token
        self.fb_token = fb_token
        self.since = since
        self.until = until
        self.storage = storage
        self.bucket = bucket
        self.file_name = ''

    def get_data(self):
        response = requests.post(f'{self.url}',
                                 data={'page_id': f'{self.page_id}',
                                       'token': f'{self.fb_token}',
                                       'since': f'{self.since}',
                                       'until': f'{self.until}'},
                                 headers={'Authorization': f'Token {self.token}'})
        return response.json()

    def load_data(self):
        response = self.get_data()
        self.file_name = response[0]["page_name"].replace(' ', '')

        with open(f"/tmp/{self.file_name}.json", "w") as file:
            json.dump(response, file)

        connection = boto3.client(self.storage)
        connection.upload_file(f"/tmp/{self.file_name}.json", self.bucket, f"{self.file_name}.json")