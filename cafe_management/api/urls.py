from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]