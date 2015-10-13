from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
        	'id', 
        	'email',
        	'first_name', 
        	'last_name',
        	'phone_number',
        	'birth_date', 
        	'password', 
        	'groups'
        )

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

