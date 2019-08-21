from rest_framework import status
from django.test import TestCase
import requests

cjToken = 'b3e6c102fae1a3be8baf3fe7e8a9315e4f4ef3d1'
#jdToken2 = ''
head = {'Authorization': 'token {}'.format(cjToken)}


class AllRestTest(TestCase):
    def setUp(self):
        self.valid_data_adserver = {
            'id': '2'
        }
        self.invalid_data_adserver = {
            'id': '444444'
        }

    def test_valid_get_one_adserver(self):
        response = requests.get('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/mediamath/adservers/'+self.valid_data_adserver['id'],
                          headers= {'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_invalid_get_one_adserver(self):
        response = requests.get('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/mediamath/adservers/'+self.invalid_data_adserver['id'],
                          headers= {'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_get_adservers(self):
        response = requests.get('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/mediamath/adservers/',
                          headers= {'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

