from rest_framework import status
from django.test import TestCase
import requests

cjToken = 'b3e6c102fae1a3be8baf3fe7e8a9315e4f4ef3d1'
#cjToken = ''
head = {'Authorization': 'token {}'.format(cjToken)}


class AllRestTest(TestCase):
    def setUp(self):
        self.valid_data_advertiser = {
            'id': '220346'
        }
        self.invalid_data_advertiser = {
            'id': '444444'
        }
    def test_get_advertisers(self):
        response1 = requests.get('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/mediamath/advertisers/',
                          headers= {'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_get_one_advertiser(self):
        response = requests.get('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/mediamath/advertisers/'+self.valid_data_advertiser['id'],
                          headers= {'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response2 = requests.get(
            'http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/mediamath/advertisers/' + self.invalid_data_advertiser['id'],
            headers={'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)



