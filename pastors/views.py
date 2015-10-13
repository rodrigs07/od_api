from rest_framework import viewsets
from pastors.serializers import PastorSerializers
from models import *

class PastorViewSet(viewsets.ModelViewSet):
    queryset = Pastors.objects.all()
    serializer_class = PastorSerializers

