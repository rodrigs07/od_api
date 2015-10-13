from rest_framework import serializers
from models import *

class PastorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pastors

