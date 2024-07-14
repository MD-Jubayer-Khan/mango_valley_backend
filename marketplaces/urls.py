from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MangoViewSet, OrderViewSet

router = DefaultRouter()
router.register('mangoes', MangoViewSet, basename='mango')
router.register('orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]