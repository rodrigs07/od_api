from django.shortcuts import render
from rest_framework.generics import(
    ListCreateAPIView
)
from pastors.serializers import PastorSerializers
from models import *
# Create your views here.

class PastorViews(ListCreateAPIView):
    queryset = Pastors.objects.all()
    serializer_class = PastorSerializers

