from django.db import models
from django.conf import settings

class Carreto(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    finished = models.BooleanField(default=False)

class Comandes(models.Model):
    STATES = (
        ('in_process', 'In progress'),
        ('sent', 'Send'),
        ('delivered', 'Delivered'),
    )
    state = models.CharField(max_length=50, choices=STATES, default='in_process')
    cart = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    products = models.ManyToManyField('Producte', through='OrderProducte')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Producte(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderProducte(models.Model):
    order = models.ForeignKey(Comandes, on_delete=models.CASCADE)
    product = models.ForeignKey(Producte, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
