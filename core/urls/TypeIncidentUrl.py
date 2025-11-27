from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import TypeIncidentViewSet



router = DefaultRouter()

router.register(r'', TypeIncidentViewSet, basename='type-incident')


urlpatterns = [
    path('', include(router.urls)),
]