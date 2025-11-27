from core.models import Quartier
from rest_framework import serializers

class QuartierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quartier
        fields = "__all__"