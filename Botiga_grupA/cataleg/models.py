from django.db import models

# Create your models here.
# Tabla Producto para la BBDD
class Producto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField()
    color = models.CharField(max_length=50)
    stock = models.IntegerField()
    fecha_publicacion = models.DateField()