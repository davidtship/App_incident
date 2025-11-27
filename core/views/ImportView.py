# core/views/ImportView.py
from rest_framework import viewsets, status
from rest_framework.response import Response
import pandas as pd
from core.models import Province, Ville, Commune, Quartier
from django.db import transaction

class ImportDataViewSet(viewsets.ViewSet):
    """
    ViewSet pour importer des données via un fichier CSV ou Excel
    """

    def create(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({'error': 'Aucun fichier fourni.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Lecture du fichier CSV ou Excel
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file)
            else:
                return Response({'error': 'Format de fichier non pris en charge.'}, status=status.HTTP_400_BAD_REQUEST)

            required_columns = ['code_province', 'province', 'ville', 'commune', 'quartier']
            if not all(col in df.columns for col in required_columns):
                return Response({'error': f'Le fichier doit contenir les colonnes : {required_columns}'}, 
                                status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                for _, row in df.iterrows():
                    # Province
                    province, _ = Province.objects.get_or_create(
                        code_province=row['code_province'],
                        defaults={'name': row['province']}
                    )
                    # Ville
                    ville, _ = Ville.objects.get_or_create(
                        code_ville=f"{province.code_province}-{row['ville']}",
                        defaults={'name': row['ville'], 'province': province}
                    )
                    # Commune
                    commune, _ = Commune.objects.get_or_create(
                        code_commune=f"{ville.code_ville}-{row['commune']}",
                        defaults={'name': row['commune'], 'ville': ville}
                    )
                    # Quartier
                    Quartier.objects.get_or_create(
                        code_quartier=f"{commune.code_commune}-{row['quartier']}",
                        defaults={'name': row['quartier'], 'commune': commune}
                    )

            return Response({'message': 'Importation réussie !'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
