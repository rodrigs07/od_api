from django.contrib.auth.models import User, Group
from users.models import *
from rest_framework import serializers

class MembroSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Membro