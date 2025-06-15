from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet

# endpoints from here

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls))
]