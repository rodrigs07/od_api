from rest_framework import serializers
from models import *

class SupervisorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Supervisors