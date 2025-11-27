from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import VilleViewSet



router = DefaultRouter()

router.register(r'villes', VilleViewSet, basename='villes')


urlpatterns = [
    path('', include(router.urls)),
]