from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import Region
from core.serializers import RegionSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [AllowAny]

