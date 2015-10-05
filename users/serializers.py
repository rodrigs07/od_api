from django.contrib.auth.models import User, Group
from users.models import *
from rest_framework import serializers

class MembroPastorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Membro 
		fields = ('id', 'username')

class MembroSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Membro
		fields = ('id', 'username', 'email', 'nome', 'sobrenome')

class PastorSerializer(serializers.HyperlinkedModelSerializer):
	membro = MembroPastorSerializer()
	class Meta:
		model = Pastor
		fields = ('id', 'membro', 'cidade', 'estado')

class SupervisorSerializer(serializers.HyperlinkedModelSerializer):
	membro = MembroPastorSerializer()
	class Meta:
		model = Supervisor
		fields = ('membro', 'pastor')