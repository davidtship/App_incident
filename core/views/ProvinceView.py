from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import Province
from core.serializers import ProvinceSerializer 
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = [AllowAny]

