from django.test import TestCase
from userprofile.models import UserProfile
from rest_framework.test import APIClient
from rest_framework import status

class UserProfileTestCase(TestCase):
    def setUp(self):
        client = APIClient()
        user_info = {
        	'email': 'teste14@ondadura.com.br', 
        	'password': '1234', 
        	'birth_date' : '1995-08-27', 
        	'phone_number': '96310352'
        }
        self.request = client.post('/users/',user_info, format='json')

    def test_example(self):
    	self.assertEqual(self.request.status_code, status.HTTP_201_CREATED)