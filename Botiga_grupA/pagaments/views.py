from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pago
from .serializers import PagoSerializer

# Create your views here.
@api_view(['POST'])
def validarTarjeta(request):
    # Obtén los datos del formulario (número de tarjeta, etc.)
    numTarjeta = request.data.get('numTarjeta', '')
    fechaCaducidad = request.data.get('fechaCaducidad', '')
    cvc = request.data.get('cvc', '')

    # Realiza la comparación con la base de datos
    try:
        tarjeta = Pago.objects.get(numTarjeta=numTarjeta)
        serializer = PagoSerializer(tarjeta)
        # Compara los campos de la tarjeta con los datos de la solicitud
        if serializer.data['fechaCaducidad'] == fechaCaducidad and serializer.data['cvc'] == cvc:
            mensaje = "¡Los datos de la tarjeta coinciden!"
        else:
            mensaje = "Los datos de la tarjeta no coinciden."
    except Pago.DoesNotExist:
        mensaje = "La tarjeta no se encuentra en la base de datos."

    return Response({'mensaje': mensaje})

@api_view(['GET','POST'])
def obtenerTarjeta(request):
    if request.method == 'GET':
        # Apartat per gestionar GET
        tarjeta = Pago.objects.all()
        serializer = PagoSerializer(tarjeta, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
