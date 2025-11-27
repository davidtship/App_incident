from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):


        password = validated_data.pop('password')
        # Création de l'utilisateur
        user = User(**validated_data)
        user.set_password(password)  # 🔹 Hash du mot de passe
        
        user.save()
        return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
        read_only_fields = ('id', 'is_active', 'is_staff')


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'role')
        read_only_fields = ('id', 'email')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        obj = self.user

        data.update({
            'id': obj.id, 
            'first_name': obj.first_name,
            'last_name': obj.last_name, 
            'email': obj.email
          
        })

        return data