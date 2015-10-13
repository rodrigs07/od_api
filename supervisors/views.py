from rest_framework import viewsets
from serializers import SupervisorsSerializers
from models import *


class SupervisorsViwesSets(viewsets.ModelViewSet):
    queryset = Supervisors.objects.all()
    serializer_class = SupervisorsSerializers


