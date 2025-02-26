from rest_framework import serializers
from .models import *

class Productserializers(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'