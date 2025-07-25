
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.viewsets import ProductViewSet, CategoryViewSet
from order.viewsets   import OrderViewSet            # se quiser expor aqui também

router = DefaultRouter()
router.register("product",  ProductViewSet,  basename="product")
router.register("category", CategoryViewSet, basename="category")
router.register("orders",   OrderViewSet,    basename="order")  # opcional

urlpatterns = [
    path("", include(router.urls)),  # ⬅️ sem grupo 'version' aqui
]
