from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
# Funcio per Llistar Productes + Funcio per Crear Productes
@api_view(['GET', 'POST'])
def getPostProductos(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
# Funcio per Llistar 1 Producte per ID + Actualtzar Producte per ID + Eliminar Producte per ID
@api_view(['GET','PUT', 'DELETE'])
def updateDeleteProducto(request, pk):
    if request.method == 'GET':
        producto = Producto.objects.filter(id=pk).first()
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        producto = Producto.objects.filter(id=pk).first()
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        producto = Producto.objects.filter(id = pk).first()
        producto.delete()
        return Response('Producto Eliminado')