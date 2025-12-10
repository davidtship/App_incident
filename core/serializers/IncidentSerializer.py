from rest_framework import serializers
from core.models import Incident, Action
from django.core.files.storage import default_storage
from .ActionSerializer import ActionSerializer
import json

class IncidentSerializer(serializers.ModelSerializer):
    # --- Lecture : inclure le nom des actions ---
    actions = ActionSerializer(many=True, read_only=True)

    # --- Écriture : accepter les IDs ---
    action_ids = serializers.PrimaryKeyRelatedField(
        queryset=Action.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    uploaded_files = serializers.ListField(
        child=serializers.FileField(max_length=None, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    picture = serializers.SerializerMethodField()

    class Meta:
        model = Incident
        fields = '__all__'  # inclut 'actions' et 'action_ids'

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
        # --- Fichiers ---
        files = validated_data.pop('uploaded_files', [])

        # --- Actions ---
        actions = validated_data.pop('action_ids', [])
        # Si actions sont envoyées en JSON string depuis React
        if isinstance(actions, str):
            actions = json.loads(actions)

        # --- Création de l'incident ---
        incident = Incident.objects.create(**validated_data)

        # Gestion fichiers
        picture_urls = []
        for f in files:
            f.name = f'incident_{incident.id}_{f.name}'
            default_storage.save(f.name, f)
            picture_urls.append(default_storage.url(f.name))
        incident.picture = picture_urls
        incident.save()

        # Ajouter les actions ManyToMany
        if actions:
            incident.actions.set(actions)

        return incident
