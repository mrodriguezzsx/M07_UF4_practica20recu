from rest_framework import serializers
from .models import Producto

# Configuracion para la vista de los productos
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'