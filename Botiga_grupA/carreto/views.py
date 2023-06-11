from decimal import Decimal
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from carreto.models import Carreto
from carreto.serializers import CarretoSerializer
from cataleg.models import Producte

class CarretoViewSet(viewsets.ModelViewSet):

    queryset = Carreto.objects.all()
    serializer_class = CarretoSerializer

    def add_product(self, request, product_id, quantity):
        product = get_object_or_404(Producte, id=product_id)
        total_price = product.price * Decimal(quantity)
        cart_item, created = Carreto.objects.get_or_create(producte=product, defaults={'cantitat': quantity, 'price': total_price})
        if not created:
            cart_item.cantitat += quantity
            cart_item.price += total_price
            cart_item.save()
        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def delete_product(self, request, product_id, quantity):
        product = get_object_or_404(Producte, id=product_id)
        cart_item = get_object_or_404(Carreto, producte=product)
        if quantity >= cart_item.cantitat:
            cart_item.delete()
        else:
            cart_item.cantitat -= quantity
            cart_item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
