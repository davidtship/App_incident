from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import User
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (UserCreateSerializer,
                           UserSerializer,
                           CustomTokenObtainPairSerializer)

from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer  # 🔹 Serializer qui accepte password
        return UserSerializer  # 🔹 Serializer pour GET /list /retrieve


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        password = request.data.get('password')
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': "Cet adresse email n'existe pas"}, status=status.HTTP_401_UNAUTHORIZED)  # utilisateur non trouvé
        if not user.check_password(password):
            return Response({'detail': 'Le mot de passe est incorrecte'}, status=status.HTTP_401_UNAUTHORIZED)  # mot de passe invalide

        return super().post(request, *args, **kwargs)
