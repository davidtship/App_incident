# core/urls/ImportUrls.py
from rest_framework.routers import DefaultRouter
from core.views.ImportView import ImportDataViewSet

router = DefaultRouter()
router.register(r'import-data', ImportDataViewSet, basename='import-data')

urlpatterns = router.urls
