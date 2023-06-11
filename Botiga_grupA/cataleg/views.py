from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def getPostProducte(request):
    if request.method == 'GET':
        # Apartat per gestionar l'apartat del GET
        queryset = TuModelo.objects.all()
        serializer = TuModeloSerializer(queryset, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        # Apartat per gestionar l'apartat del Post
        serializer = TuModeloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)