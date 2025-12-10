from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import (
    ProvinceViewSet,
    VilleViewSet,
    QuartierViewSet,
    CommuneViewSet,
    IncidentAPIView,  # APIView
    IncidentCategoryViewSet,
    TypeIncidentViewSet,
    RegionViewSet,
    SchoolViewSet,
    SchoolCategoryViewSet,
    ImportDataViewSet,
    ActionViewSet
)

# Crée un router pour les ViewSets
router = DefaultRouter()
router.register(r'provinces', ProvinceViewSet, basename='province')
router.register(r'villes', VilleViewSet, basename='ville')
router.register(r'quartiers', QuartierViewSet, basename='quartier')
router.register(r'communes', CommuneViewSet, basename='commune')
router.register(r'incident-categories', IncidentCategoryViewSet, basename='incident-category')
router.register(r'incident-types', TypeIncidentViewSet, basename='incident-types')
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'school-categories', SchoolCategoryViewSet, basename='school-category')
router.register(r'region', RegionViewSet, basename='region')
router.register(r'actions', ActionViewSet, basename='action')
router.register(r'import', ImportDataViewSet, basename='import')

# URLs finales
urlpatterns = [
    path('incidents/', IncidentAPIView.as_view(), name='incident-list'),  # APIView pour incidents
    path('', include(router.urls)),  # le reste des ViewSets
]
