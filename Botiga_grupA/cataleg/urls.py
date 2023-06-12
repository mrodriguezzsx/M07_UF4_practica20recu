from django.urls import path
from . import views

urlpatterns = [
    # Ruta per accedir a la view per Llistar Productes i Crear Productes
    path('productos/', views.getPostProductos, name='getPost'),

    # Ruta per accedir a la view per Actualitzar Producte per ID i Eliminar Producte per ID
    path('productos/<int:pk>/', views.updateDeleteProducto, name='updateDelete'),
]