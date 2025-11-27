from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import CommuneViewSet



router = DefaultRouter()

router.register(r'', CommuneViewSet, basename='commune')


urlpatterns = [
    path('', include(router.urls)),
]