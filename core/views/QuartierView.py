from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import Quartier
from core.serializers import QuartierSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class QuartierViewSet(viewsets.ModelViewSet):
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer
    permission_classes = [AllowAny]

