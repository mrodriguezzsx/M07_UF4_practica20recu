from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
@api_view(['GET'])
def verProductos(request):
        # Apartat per gestionar l'apartat del GET
        queryset = Producto.objects.all()
        serializer = ProductoSerializer(queryset, many=True)
        return Response(serializer.data)