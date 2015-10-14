from rest_framework import viewsets
from serializers import ShepherdsSerializers
from models import *


class ShepherdsViwesSets(viewsets.ModelViewSet):
    queryset = Shepherds.objects.all()
    serializer_class = ShepherdsSerializers


