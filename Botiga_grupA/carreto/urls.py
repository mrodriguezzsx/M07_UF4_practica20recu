from .views import CarretoViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('carreto', CarretoViewSet)

urlpatterns = [
    path('carreto/', CarretoViewSet.as_view({'get': 'list'}), name='carreto-list'),
    path('carreto/destroy/<int:pk>/', CarretoViewSet.as_view({'delete': 'destroy'}), name='carreto-destroy'),
    path('carreto/add/', CarretoViewSet.as_view({'post': 'create'}), name='carreto-add'),
    path('carreto/<pk>/add_product/<product_id>/', CarretoViewSet.as_view({'post': 'add_product'}), name='carreto-add-product'),
    path('carreto/delete/product', CarretoViewSet.as_view({'post': 'delete_product'}), name='carreto-delete-product'),
    path('carreto/delete/<int:pk>/', CarretoViewSet.as_view({'delete': 'destroy'}), name='carreto-delete'),
]