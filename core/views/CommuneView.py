from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import Commune
from core.serializers import CommuneSerializer 
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class CommuneViewSet(viewsets.ModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer
    permission_classes = [AllowAny]

