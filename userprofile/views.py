from rest_framework import viewsets
from userprofile.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import Group
from models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer