from django.urls import path
from . import views

urlpatterns = [
    path('pagament/', views.validarTarjeta, name='validar'),
    path('targeta/', views.obtenerTarjeta, name="obtener")
]