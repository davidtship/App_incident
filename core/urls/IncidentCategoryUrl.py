from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import IncidentCategoryViewSet



router = DefaultRouter()

router.register(r'', IncidentCategoryViewSet, basename='incident-category')


urlpatterns = [
    path('', include(router.urls)),
]