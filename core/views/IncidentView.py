from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
from core.models import Incident
from core.serializers import IncidentSerializer

class IncidentAPIView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]  # pour gérer FormData + fichiers

    def get(self, request):
        incidents = Incident.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_incidents = paginator.paginate_queryset(incidents, request)
        serializer = IncidentSerializer(paginated_incidents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IncidentSerializer(data=request.data)
        
        if serializer.is_valid():
            incident = serializer.save()
            return Response(IncidentSerializer(incident).data, status=status.HTTP_201_CREATED)
        
        # Si invalid, afficher les erreurs pour debug
        print("=== Serializer errors ===")
        for field, errors in serializer.errors.items():
            print(f"Champ problématique : {field} -> Erreurs : {errors}")
        print("========================")
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
