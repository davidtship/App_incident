from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import QuartierViewSet



router = DefaultRouter()

router.register(r'', QuartierViewSet, basename='quartier')


urlpatterns = [
    path('', include(router.urls)),
]