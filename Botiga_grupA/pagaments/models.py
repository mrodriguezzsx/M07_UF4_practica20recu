from django.db import models

# Create your models here.
class Pago(models.Model):
    numTarjeta = models.BigIntegerField()
    fechaCaducidad = models.DateField()
    cvc = models.IntegerField(max_length=3)