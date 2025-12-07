from rest_framework import serializers
from core.models import Incident
from django.core.files.storage import default_storage

class IncidentSerializer(serializers.ModelSerializer):
    actionTaken = serializers.ListField(child=serializers.CharField(), required=False)
    uploaded_files = serializers.ListField(
        child=serializers.FileField(max_length=None, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    picture = serializers.SerializerMethodField()
    state = serializers.BooleanField()

    class Meta:
        model = Incident
        fields = '__all__'

    def get_picture(self, obj):
        request = self.context.get('request')
        if not obj.picture:
            return []
        urls = []
        for pic in obj.picture:
            url = pic
            if request and not url.startswith('http'):
                url = request.build_absolute_uri(url)
            urls.append(url)
        return urls

    def create(self, validated_data):
        files = validated_data.pop('uploaded_files', [])
        actions = validated_data.pop('actionTaken', [])

        incident = Incident.objects.create(**validated_data)

        picture_urls = []
        for f in files:
            f.name = f'incident_{incident.id}_{f.name}'
            default_storage.save(f.name, f)
            picture_urls.append(default_storage.url(f.name))

        incident.picture = picture_urls
        incident.actionTaken = actions
        incident.save()
        return incident
