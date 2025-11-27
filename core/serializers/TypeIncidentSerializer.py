from core.models import TypeIncident
from rest_framework import serializers

class TypeIncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeIncident
        fields = "__all__"