from rest_framework import serializers
from core.models import Incident
from django.core.files.storage import default_storage

class IncidentSerializer(serializers.ModelSerializer):
    # Actions prises (liste de strings)
    actionTaken = serializers.ListField(child=serializers.CharField(), required=False)
    
    # Fichiers images
    picture = serializers.ListField(
        child=serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True),
        required=False
    )

    state = serializers.BooleanField()

    class Meta:
        model = Incident
        fields = '__all__'

    def create(self, validated_data):
        pictures = validated_data.pop('picture', [])
        actions = validated_data.pop('actionTaken', [])

        # Création de l'incident
        incident = Incident.objects.create(**validated_data)
        
        # Sauvegarde des fichiers et création des URLs
        picture_urls = []
        for pic in pictures:
            pic.name = f'incident_{incident.id}_{pic.name}'
            default_storage.save(pic.name, pic)
            picture_urls.append(default_storage.url(pic.name))

        incident.picture = picture_urls
        incident.actionTaken = actions
        incident.save()
        return incident
