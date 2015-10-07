from django.test import TestCase
from userprofile.models import UserProfile
from rest_framework.test import APIClient
from rest_framework import status

class UserProfileTestCase(TestCase):
    def setUp(self):
        client = APIClient()
        self.request = client.post('/users/', {'email': 'teste14@ondadura.com.br', 'password': '1234' }, format='json')

    def test_example(self):
    	self.assertEqual(self.request.status_code, status.HTTP_201_CREATED)