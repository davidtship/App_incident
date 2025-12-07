from rest_framework import serializers
from core.models import Incident
from django.core.files.storage import default_storage

class IncidentSerializer(serializers.ModelSerializer):
    # Actions prises
    actionTaken = serializers.ListField(child=serializers.CharField(), required=False)
    
    # Champ pour upload de fichiers (write_only pour POST/PUT)
    files = serializers.ListField(
        child=serializers.FileField(max_length=None, allow_empty_file=False, use_url=True),
        write_only=True,
        required=False
    )

    # Champ pour GET : retourne les URLs absolues des médias
    picture = serializers.SerializerMethodField()
    state = serializers.BooleanField()

    class Meta:
        model = Incident
        fields = '__all__'

    def get_picture(self, obj):
        """
        Retourne une liste d'URLs absolues pour tous les médias.
        """
        if not obj.picture:
            return []

        request = self.context.get('request')
        urls = []

        for pic in obj.picture:
            if isinstance(pic, str):
                # Nettoie les doublons /media/
                clean_path = pic.replace('//media/', '/media/').lstrip('/')
                url = default_storage.url(clean_path)

                # Transforme en URL absolue si request est disponible
                if request and not url.startswith('http'):
                    url = request.build_absolute_uri(url)

                urls.append(url)

        return urls

    def create(self, validated_data):
        """
        Crée un incident et sauvegarde les fichiers médias,
        en stockant des URLs correctes dans picture.
        """
        files = validated_data.pop('files', [])
        actions = validated_data.pop('actionTaken', [])

        incident = Incident.objects.create(**validated_data)

        media_urls = []
        for f in files:
            filename = f'incident_{incident.id}_{f.name}'
            default_storage.save(filename, f)
            url = default_storage.url(filename)
            request = self.context.get('request')
            if request and not url.startswith('http'):
                url = request.build_absolute_uri(url)
            media_urls.append(url)

        incident.picture = media_urls
        incident.actionTaken = actions
        incident.save()

        return incident
