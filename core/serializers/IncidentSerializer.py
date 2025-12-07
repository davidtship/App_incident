from rest_framework import serializers
from core.models import Incident
from django.core.files.storage import default_storage

class IncidentSerializer(serializers.ModelSerializer):
    actionTaken = serializers.ListField(child=serializers.CharField(), required=False)

    # On accepte les fichiers envoyés pour l'upload
    files = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False
    )

    # On renvoie les URLs pour GET
    picture = serializers.SerializerMethodField()
    state = serializers.BooleanField()

    class Meta:
        model = Incident
        fields = '__all__'

    def get_picture(self, obj):
        if not obj.picture:
            return []
        request = self.context.get('request')
        urls = []
        for pic in obj.picture:
            if isinstance(pic, str):
                clean_path = pic.replace('//media/', '/media/').lstrip('/')
                url = default_storage.url(clean_path)
                if request and not url.startswith('http'):
                    url = request.build_absolute_uri(url)
                urls.append(url)
        return urls

    def create(self, validated_data):
        files = validated_data.pop('files', [])
        actions = validated_data.pop('actionTaken', [])

        incident = Incident.objects.create(**validated_data)

        picture_urls = []
        for f in files:
            filename = f'incident_{incident.id}_{f.name}'
            default_storage.save(filename, f)
            url = default_storage.url(filename)
            request = self.context.get('request')
            if request and not url.startswith('http'):
                url = request.build_absolute_uri(url)
            picture_urls.append(url)

        incident.picture = picture_urls
        incident.actionTaken = actions
        incident.save()
        return incident
