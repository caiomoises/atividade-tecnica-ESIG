from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        login = attrs.get("username")
        password = attrs.get("password")

        # Verifica se é email ou username
        if "@" in login:
            try:
                user_instance = User.objects.get(email=login)
            except User.DoesNotExist:
                raise serializers.ValidationError("Nenhum usuário encontrado com este e-mail.")
        else:
            try:
                user_instance = User.objects.get(username=login)
            except User.DoesNotExist:
                raise serializers.ValidationError("Nenhum usuário encontrado com este username.")

        # Autentica usando o username correto
        user = authenticate(username=user_instance.username, password=password)
        if not user:
            raise serializers.ValidationError("Credenciais inválidas.")

        # Chama o validate original com o username correto
        validated_data = super().validate({
            "username": user_instance.username,
            "password": password,
        })

        return validated_data
