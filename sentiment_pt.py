import pickle
import requests
import os.path
import spacy

spacy.load('pt_core_news_sm')
stop_words = list(spacy.lang.pt.stop_words.STOP_WORDS)
data_file_name = 'sentiement_pt.csv'

if(not os.path.exists(data_file_name)):
  url = 'http://localhost:8000/api/v1/tripadvisor/scraper/'
  data = {
      'hotels': 'https://www.tripadvisor.com.br/Attraction_Review-g34515-d130846-Reviews-Disney_Springs-Orlando_Florida.html',
      'language': 'pt'
  }
  headers = {
      'Authorization': 'Token e91d9f6c9810bf07b419b2a141d6435d241c4e9f'
  }

  response = requests.post(url, data=data, headers=headers)
  data = response.json()
  data = data[0]
  delimiter = ';'
  csv = ''
  for review in data['reviews']:
    csv += f'{data["destination_name"]}{delimiter}{data["total_reviews"]}{delimiter}{data["ratings"]}{delimiter}{review["review_date"]}{delimiter}'\
      f'{review["review_rating"]}{delimiter}{review["review_header"]}{delimiter}{review["review_author"]}{delimiter}{review["review_text"]}\n'
  data_file = open(data_file_name, 'a', encoding='utf8')
  data_file.write(csv)
  data_file.close()
else:
  data_file = open(data_file_name, 'rb')
  data = pickle.load(data_file)

#print(data)
