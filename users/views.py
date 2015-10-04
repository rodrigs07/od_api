from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from users.serializers import *

class MembroViewSet(viewsets.ModelViewSet):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer