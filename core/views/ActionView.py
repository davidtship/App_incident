from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import Action
from core.serializers import ActionSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [AllowAny]

