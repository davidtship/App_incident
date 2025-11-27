from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import School
from core.serializers import SchoolSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]
