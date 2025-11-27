from core.models import Province
from rest_framework import serializers

class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = "__all__"