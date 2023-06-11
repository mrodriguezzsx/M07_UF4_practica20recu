from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.getPostProductos, name='getPost'),
    path('productos/<int:pk>/', views.updateDeleteProducto, name='updateDelete'),
]