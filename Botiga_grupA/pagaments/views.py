from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pago
from .serializers import PagoSerializer

# Create your views here.
# Funcio per Validar les targetes ja creades.
@api_view(['POST'])
def validarTarjeta(request):
    # Obte les dades del "formulari" (numero de targeta, etc.)
    numTarjeta = request.data.get('numTarjeta', '')
    fechaCaducidad = request.data.get('fechaCaducidad', '')
    cvc = request.data.get('cvc', '')

    # Realitza la comparacio amb la base de dades
    try:
        # Agafa el numero de targeta
        tarjeta = Pago.objects.get(numTarjeta=numTarjeta)

        # Pasa el numero de targeta per la BBDD
        serializer = PagoSerializer(tarjeta)

        # Compara els camps de la targeta amb les dades de la sol·licitud
        if serializer.data['fechaCaducidad'] == fechaCaducidad and serializer.data['cvc'] == cvc:
            mensaje = "¡Los datos de la tarjeta coinciden!"
        else:
            mensaje = "Los datos de la tarjeta no coinciden."
    except Pago.DoesNotExist:
        mensaje = "La tarjeta no se encuentra en la base de datos."

    return Response({'mensaje': mensaje})

# Funcio extra(Per ajudar a posar les dades)
# Funcio que Llista les targetes ja creades + Crear targetes noves
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
