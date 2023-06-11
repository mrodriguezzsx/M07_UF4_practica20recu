from rest_framework import serializers
from .models import Comandes, Producte, Carreto, OrderProducte

# Serializador para el modelo de Producto
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = '__all__'

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer() 

    class Meta:
        model = OrderProducte
        fields = ('id','marca', 'modelo', 'precio', 'color', 'stock', 'fecha_publicacion')

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, source='orderproduct_set')

    class Meta:
        model = Comandes
        fields = ('id', 'state', 'order_products', 'created_at', 'updated_at')

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comandes
        fields = ('id', 'state', 'created_at', 'updated_at')

class CarSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, source='order_set') 
    class Meta:
        model = Carreto
        fields = ('id', 'created_at', 'updated_at', 'finished', 'orders')

class HistoricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fields = ('finished') 