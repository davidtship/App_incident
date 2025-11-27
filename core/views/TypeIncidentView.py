from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import TypeIncident
from core.serializers import TypeIncidentSerializer 
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class TypeIncidentViewSet(viewsets.ModelViewSet):
    queryset = TypeIncident.objects.all()
    serializer_class = TypeIncidentSerializer
    permission_classes = [AllowAny]

