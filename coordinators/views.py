from rest_framework import viewsets
from serializers import CoordinatorsSerializers
from models import *


class CoordinatorsViwesSets(viewsets.ModelViewSet):
    queryset = Coordinators.objects.all()
    serializer_class = CoordinatorsSerializers


