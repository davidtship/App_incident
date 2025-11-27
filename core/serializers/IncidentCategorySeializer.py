from core.models import IncidentCategory
from rest_framework import serializers

class IncidentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = IncidentCategory
        fields = "__all__"