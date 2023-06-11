from rest_framework import serializers
from carreto.models import Carreto

class CarretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fields = '__all__'