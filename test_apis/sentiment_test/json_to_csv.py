import csv
import json
from datetime import date as python_date
from dateutil.rrule import rrule, DAILY
from classifier import *
import re
from stop_words import get_stop_words


def read_json(path):
    try:
        with open(path, 'r', encoding="utf8") as file:
            response_json = json.load(file)
        return response_json
    except Exception as e:
        print(f"Error to read JSON File: {e}")


def parse_json_to_csv(name, json):
    with open(f"{name}.csv", mode='w', newline='', encoding='utf-8') as file:
        employee_writer = csv.writer(file, delimiter=',')
        columns = ['medium', 'channel_name', 'channel_id', 'date_since',
                   'date_until', 'date', 'video_id', 'video_name',
                   'comment_text', 'polarity', 'word', 'frequency']
        employee_writer.writerow(columns)
        for m in json:
            medium = m['medium']
            channel_name = m['channel_name']
            channel_id = m['channel_id']
            date_since = m['date_since']
            date_until = m['date_until']
            for results in json[0]['results']:
                date = results['date']
                for comment in results['comments']:
                    video_id = comment['video_id']
                    video_name = comment['video_name']
                    comment_text = comment['comment_text']
                    polarity = comment['polarity']
                    for frequency in results['frequency_words']:
                        word = frequency['word']
                        freq = frequency['frequency']
                        string = f"{medium}|{channel_name}|{channel_id}|{date_since}|{date_until}|"\
                                 f"{date}|"\
                                 f"{video_id}|{video_name}|{comment_text}|{polarity}|"\
                                 f"{word}|{freq}"
                        response = string.split('|')
                        employee_writer.writerow(response)


def transform_date(date):
    split_original_time = date.split('-')
    response = python_date(int(split_original_time[0]),
                           int(split_original_time[1]),
                           int(split_original_time[2]))
    return response


def clean_string(string):
    stop_words = get_stop_words('spanish')
    string = re.sub(r"\b[a-zA-Z]{1}\b", '', string)  # Remove Special Characters
    for word in stop_words:
        if re.findall(fr'\b({word})\b', string):
            string = re.sub(fr"\b({word})\b", '', string)
    return string


def get_frequency_words(string):
    string = clean_string(string)
    words_list = string.split()
    words_frequency = [words_list.count(word) for word in words_list]
    response = sorted(set(zip(words_list, words_frequency)), key=lambda x: x[1], reverse=True)
    return response


if __name__ == '__main__':
    data_crude = read_json('instagram_post.json')[0]
    since = transform_date(data_crude['since'])
    until = transform_date(data_crude['until'])

    clf = SentimentClassifier()
    json_exit = []
    json_exit = [
                    {
                        'medium': '',
                        'page_name': '',
                        'page_id': '',
                        'date_since': '',
                        'date_until': '',
                        'results': []
                    }
                ]

    json_exit[0]['medium'] = 'facebook'
    json_exit[0]['page_name'] = data_crude['page_name']
    json_exit[0]['page_id'] = data_crude['page_id']
    json_exit[0]['date_since'] = data_crude['since']
    json_exit[0]['date_until'] = data_crude['until']

    for day in rrule(DAILY, dtstart=since, until=until):
        date_temp = day.strftime("%Y-%m-%d")
        result_total_temp = {
                        'date': date_temp,
                        'comments': [],
                        'frecuency_words': []
                      }
        total_coments_by_day = ''
        for result in data_crude['results']:
            post_id = result['post_id']
            post_name = result['post_name']
            result_post_temp = {
                                'post_id': post_id,
                                'post_name': post_name,
                                'results': []
                                }
            for comment in result['comments']:
                if comment['created_time'] == date_temp:
                    comment_text = comment['comment_text']
                    polarity = clf.predict(comment_text)
                    comment_temp = {
                                        'comment_text': comment_text,
                                        'polarity': polarity
                                    }
                    result_post_temp['results'].append(comment_temp)
                    total_coments_by_day += comment_text

            if len(result_post_temp['results']) > 0:
                result_total_temp['comments'].append(result_post_temp)

        if total_coments_by_day != '':
            for frecuency_words in get_frequency_words(clean_string(total_coments_by_day))[:5]:
                frecuency_words_temp = {
                                            'word': frecuency_words[0],
                                            'frecuency': frecuency_words[1]
                                        }
                result_total_temp['frecuency_words'].append(frecuency_words_temp)

        if len(result_total_temp['comments']) > 0:
            json_exit[0]['results'].append(result_total_temp)

    print(json.dumps(json_exit, indent=4))





