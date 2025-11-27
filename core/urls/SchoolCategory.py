from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import SchoolCategoryViewSet



router = DefaultRouter()

router.register(r'', SchoolCategoryViewSet, basename='school-category')


urlpatterns = [
    path('', include(router.urls)),
]