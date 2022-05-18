from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class JokesTests(APITestCase):

    def setUp(self):
        self.url = reverse('chucknorris:random-list')

    def test_successful_status_code(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_jokes_not_none(self):
        response = self.client.get(self.url, format='json')
        self.assertNotEqual(response.data['jokes'], None)

    def test_length_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(len(response.data['jokes']), 15)