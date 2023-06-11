from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Comandes, Carreto, OrderProducte
from .serializers import OrderSerializer, CarSerializer
from rest_framework.decorators import action
from django.http import Http404
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


class OrderPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
        
class CartViewSet(viewsets.ModelViewSet):
    queryset = Carreto.objects.all() 
    pagination_class = OrderPagination 
    serializer_class = CarSerializer 
    permission_classes = [permissions.IsAuthenticated] 

    def get_object(self):
            user = self.request.user 
            try:
                carrito = Carreto.objects.get(user=user) 
                return carrito
            except Carreto.DoesNotExist:
                raise Http404 
            
    def list(self, request):
        if request.user.is_authenticated:
            if self.queryset.filter(user=request.user, finished=False):
                incomplete_carts = self.queryset.filter(user=request.user, finished=False)
                serializer = self.get_serializer(incomplete_carts, many=True)
                return Response(serializer.data)


    def retrieve(self, request, pk=None):
            if request.user.is_authenticated:
                try:
                    carrito = Carreto.objects.get(pk=pk, user=request.user)
                except Carreto.DoesNotExist:
                    return Response({"message": "Acceso a carrito"}, status=status.HTTP_404_NOT_FOUND)
                serializer = self.get_serializer(carrito)
                return Response(serializer.data)

    def destroy(self, request, pk=None):
        if request.user.is_authenticated:
            try:
                carrito = Carreto.objects.get(pk=pk, user=request.user)
            except Carreto.DoesNotExist:
                return Response({"message": "Acceso a carrito"}, status=status.HTTP_404_NOT_FOUND)
            carrito.delete()
            return Response({"message": "Carrito eliminado"}, status=status.HTTP_204_NO_CONTENT)

        
    @action(detail=False, methods=['get', 'post'])
    def historics(self, request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                carrito = Carreto.objects.filter(user=request.user, finished=False).first()
                if carrito:
                    carrito.finished = True
                    carrito.save()
            complete_carts = self.queryset.filter(user=request.user, finished=True)
            serializer = self.get_serializer(complete_carts, many=True)
            return Response(serializer.data)


    @action(detail=False, methods=['delete'])
    def remove_producte(self, request, product_id=None, **kwargs):
        if request.user.is_authenticated:
            try:
                carrito = self.get_object()
                order_product = OrderProducte.objects.filter(
                    order__cart=carrito,
                    order__cart__user=request.user, 
                    product_id=product_id
                ).first()

                if not order_product:
                    return Response({'message': 'El producto no está en el carrito.'}, status=status.HTTP_400_BAD_REQUEST)
                
                order_product.delete()
                return Response({'message': 'Producto eliminado'})

            except Carreto.DoesNotExist:
                return Response({"message": "Acceso a carrito"}, status=status.HTTP_404_NOT_FOUND)

        
    @action(detail=False, methods=['get'], serializer_class=OrderSerializer)
    def registro(self, request):
        if request.user.is_authenticated:
            in_process_orders = Comandes.objects.filter(state='In progress', cart__user=request.user).order_by('-created_at')
            in_process_paginated_orders = self.paginate_queryset(in_process_orders) 
            
            sent_orders = Comandes.objects.filter(state='Send', cart__user=request.user).order_by('-created_at')
            sent_paginated_orders = self.paginate_queryset(sent_orders) 
            
            delivered_orders = Comandes.objects.filter(state='Delivered', cart__user=request.user).order_by('-created_at')
            delivered_paginated_orders = self.paginate_queryset(delivered_orders) 

            in_process_serializer = self.get_serializer(in_process_paginated_orders, many=True)
            sent_serializer = self.get_serializer(sent_paginated_orders, many=True)
            delivered_serializer = self.get_serializer(delivered_paginated_orders, many=True)

            return Response({
                'In progress': in_process_serializer.data,
                'Send': sent_serializer.data,
                'Delivered': delivered_serializer.data
            })
