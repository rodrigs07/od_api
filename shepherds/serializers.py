from rest_framework import serializers
from models import *

class ShepherdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shepherds