from rest_framework import serializers
from core.models import Incident
from django.core.files.storage import default_storage
from urllib.parse import quote

class IncidentSerializer(serializers.ModelSerializer):
    actionTaken = serializers.ListField(child=serializers.CharField(), required=False)
    picture = serializers.SerializerMethodField()
    state = serializers.BooleanField()

    class Meta:
        model = Incident
        fields = '__all__'

    def get_picture(self, obj):
        """
        Retourne des URLs absolues propres pour les images.
        """
        if not obj.picture:
            return []

        request = self.context.get('request')
        urls = []

        for pic in obj.picture:
            if isinstance(pic, str):
                # Nettoyer les doublons /media/ et encoder correctement les caractères spéciaux
                clean_path = pic.replace('//media/', '/media/').lstrip('/')
                clean_path = quote(clean_path, safe='/')  # encode correctement espaces et caractères spéciaux

                # URL relative via default_storage
                url = default_storage.url(clean_path)

                # URL absolue si request est présent
                if request and not url.startswith('http'):
                    url = request.build_absolute_uri(url)

                urls.append(url)

        return urls

    def create(self, validated_data):
        pictures = validated_data.pop('picture', [])
        actions = validated_data.pop('actionTaken', [])

        incident = Incident.objects.create(**validated_data)

        # Sauvegarde des fichiers et stockage uniquement du chemin relatif
        picture_urls = []
        for pic in pictures:
            pic.name = f'incident_{incident.id}_{pic.name}'
            default_storage.save(pic.name, pic)
            picture_urls.append(f'{pic.name}')  # stocke juste le chemin relatif sans /media/ dupliqué

        incident.picture = picture_urls
        incident.actionTaken = actions
        incident.save()
        return incident
