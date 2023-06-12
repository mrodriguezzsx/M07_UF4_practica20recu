from django.db import models

# Create your models here.
# Creacio de la Taula Pago per a la BBDD
class Pago(models.Model):
    numTarjeta = models.BigIntegerField()
    fechaCaducidad = models.DateField()
    cvc = models.IntegerField(max_length=3)