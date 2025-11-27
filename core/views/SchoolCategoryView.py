from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import SchoolCategory
from core.serializers import SchoolCategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class SchoolCategoryViewSet(viewsets.ModelViewSet):
    queryset = SchoolCategory.objects.all()
    serializer_class = SchoolCategorySerializer
    permission_classes = [AllowAny]
