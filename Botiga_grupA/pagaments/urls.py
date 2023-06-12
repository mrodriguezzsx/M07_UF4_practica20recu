from django.urls import path
from . import views

urlpatterns = [
    # Ruta que accedeix a la view de la validacio
    path('pagament/', views.validarTarjeta, name='validar'),

    # Ruta que accedeix a la creacio i al llistat de Targetes
    path('targeta/', views.obtenerTarjeta, name="obtener"),
]