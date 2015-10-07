from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

