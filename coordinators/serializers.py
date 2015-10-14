from rest_framework import serializers
from models import *

class CoordinatorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coordinators