from rest_framework import status
from django.test import TestCase
import requests

cjToken = 'b3e6c102fae1a3be8baf3fe7e8a9315e4f4ef3d1'
# jdToken2 = ''
head = {'Authorization': 'token {}'.format(cjToken)}


class AllRestTest(TestCase):
    def setUp(self):
        self.valid_data_metrics_and_dimensions = {
            'view_id': '168520073',
            'metrics': 'sessions,users',
            'dimensions': 'country,browser',
            'dateRanges': '2019-02-10,2019-03-11'
        }

        self.valid_data_multiperiods = {
            'view_id': '168520073',
            'metrics': 'pageviews,sessions',
            'dimensions': 'pageTitle',
            'dateRanges': '2019-01-10,2019-02-09,2019-02-10,2019-03-11'
        }

        self.valid_data_segments = {
            'view_id': '168520073',
            'metrics': 'sessions',
            'dimensions': 'segment,browser',
            'dateRanges': '2019-02-10,2019-03-11',
            'segment': 'browser,EXACT,Safari'
        }

        self.invalid_data_metrics_and_dimensions = {
            'view_id': '16852007',
            'metrics': 'sessions,users',
            'dimensions': 'country,browser',
            'dateRanges': '2019-02-10,2019-03-11'
        }

        self.invalid_data_multiperiods = {
            'view_id': '16852007',
            'metrics': 'pageviews,sessions',
            'dimensions': 'pageTitle',
            'dateRanges': '2019-01-10,2019-02-09,2019-02-10,2019-03-11'
        }

        self.invalid_data_segments = {
            'view_id': '16852007',
            'metrics': 'sessions',
            'dimensions': 'segment,browser',
            'dateRanges': '2019-02-10,2019-03-11',
            'segment': 'browser,EXACT,Safari'
        }

    def test_valid_metrics_and_dimensions(self):
        response = requests.post('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/analytics/metrics&dimensions/',
                                 data=self.valid_data_metrics_and_dimensions,
                                 headers={'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_multiperiods(self):
        response = requests.post('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/analytics/multiperiods/',
                                 data=self.valid_data_multiperiods,
                                 headers={'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_metrics_and_dimensions(self):
        response = requests.post('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/analytics/metrics&dimensions/',
                                 data=self.invalid_data_metrics_and_dimensions,
                                 headers={'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_multiperiods(self):
        response = requests.post('http://ec2-52-206-110-32.compute-1.amazonaws.com/api/v1/analytics/multiperiods/',
                                 data=self.invalid_data_multiperiods,
                                 headers={'Authorization': 'token {}'.format(cjToken)})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


