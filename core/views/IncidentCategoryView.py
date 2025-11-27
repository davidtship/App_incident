from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import IncidentCategory
from core.serializers import IncidentCategorySerializer 
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class IncidentCategoryViewSet(viewsets.ModelViewSet):
    queryset = IncidentCategory.objects.all()
    serializer_class = IncidentCategorySerializer
    permission_classes = [AllowAny]

