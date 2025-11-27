from core.models import SchoolCategory
from rest_framework import serializers

class SchoolCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolCategory
        fields = "__all__"