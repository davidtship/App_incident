from rest_framework import serializers
from core.models import Incident
from django.core.files.storage import default_storage

class IncidentSerializer(serializers.ModelSerializer):
    # Actions prises (liste de strings)
    actionTaken = serializers.ListField(child=serializers.CharField(), required=False)
    
    # Fichiers images : pour le GET on retourne les URLs
    picture = serializers.SerializerMethodField()

    state = serializers.BooleanField()

    class Meta:
        model = Incident
        fields = '__all__'

    def get_picture(self, obj):
        """
        Retourne la liste des URLs pour les images de l'incident.
        """
        if not obj.picture:
            return []
        # Si la liste contient déjà des URLs
        if all(isinstance(p, str) and p.startswith('http') for p in obj.picture):
            return obj.picture
        # Sinon, générer les URLs via default_storage
        urls = []
        for pic in obj.picture:
            try:
                urls.append(default_storage.url(pic))
            except Exception:
                pass
        return urls

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
