from rest_framework.generics import(
    ListCreateAPIView
)
from userprofile.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import Group
from models import *

class UserViewSet(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer