from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import ProvinceViewSet



router = DefaultRouter()

router.register(r'', ProvinceViewSet, basename='provinces')


urlpatterns = [
    path('', include(router.urls)),
]