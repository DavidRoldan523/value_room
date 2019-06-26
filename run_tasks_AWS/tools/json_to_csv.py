import csv
import boto3


class JsonToCsv:
    def __init__(self, bucket, json, storage):
        self.bucket = bucket
        self.json = json
        self.storage = storage

    def load_data(self):
        file_name = self.json[0]["page_name"].replace(' ', '') + self.json[0]["medium"]
        with open(f"/tmp/{file_name}.csv", mode='w', newline='', encoding='utf8') as file:
            row_csv = csv.writer(file, delimiter=',')
            columns = ['medium', 'page_name', 'page_id', 'date_since',
                       'date_until', 'date', 'post_id', 'post_name',
                       'comment_text', 'polarity', 'word', 'frequency']
            row_csv.writerow(columns)
            for m in self.json:
                medium = m['medium']
                page_name = m['page_name']
                page_id = m['page_id']
                date_since = m['date_since']
                date_until = m['date_until']
                for results in self.json[0]['results']:
                    date = results['date']
                    for comment in results['comments']:
                        post_id = comment['post_id']
                        post_name = comment['post_name']
                        for post in comment['results']:
                            comment_text = post['comment_text']
                            polarity = post['polarity']
                            for frequency in results['frequency_words']:
                                word = frequency['word']
                                freq = frequency['frequency']
                                string = f"{medium}|{page_name}|{page_id}|{date_since}|{date_until}|" \
                                    f"{date}|" \
                                    f"{post_id}|{post_name}|{comment_text}|{polarity}|" \
                                    f"{word}|{freq}"
                                response = string.split('|')
                                row_csv.writerow(response)

        connection = boto3.client(self.storage)
        connection.upload_file(f"/tmp/{file_name}.csv", self.bucket, f"{file_name}.csv")