from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import Ville
from core.serializers import VilleSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class VilleViewSet(viewsets.ModelViewSet):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer
    permission_classes = [AllowAny]  # 🔹 Tout le monde peut accéder

