from django.urls import path, include
from rest_framework import routers
from .views import CartViewSet


router = routers.DefaultRouter()
router.register(r'Comandes', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('Orders/<int:pk>/remove_product/<int:product_id>/', CartViewSet.as_view({'delete': 'remove_product'})),
]
