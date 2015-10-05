from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from users.serializers import *

class MembroViewSet(viewsets.ModelViewSet):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

class PastorViewSet(viewsets.ModelViewSet):
    queryset = Pastor.objects.all()
    serializer_class = PastorSerializer

class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer