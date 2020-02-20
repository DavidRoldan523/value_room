import pickle
import requests
import os.path
import spacy

spacy.load('pt_core_news_sm')
stop_words = list(spacy.lang.pt.stop_words.STOP_WORDS)
data_file_name = 'sentiement.txt'

if(not os.path.exists(data_file_name)):
  url = 'http://localhost:8000/api/v1/tripadvisor/scraper/'
  data = {
      'hotels': 'https://www.tripadvisor.co/Hotel_Review-g297476-d307529-Reviews-Decameron_Cartagena-Cartagena_Cartagena_District_Bolivar_Department.html',
      'language': 'pt'
  }
  headers = {
      'Authorization': 'Token e91d9f6c9810bf07b419b2a141d6435d241c4e9f'
  }

  response = requests.post(url, data=data, headers=headers)
  data = response.json()
  data_file = open(data_file_name, 'wb')
  pickle.dump(data, data_file)
else:
  data_file = open(data_file_name, 'rb')
  data = pickle.load(data_file)

#print(data)
