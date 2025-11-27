from core.models import Commune
from rest_framework import serializers

class CommuneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commune
        fields = "__all__"