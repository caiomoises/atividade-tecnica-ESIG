from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import AllowAny

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]  # Permite acesso sem autenticação
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'token': response.data['access'], 
            'refresh': response.data['refresh']
        }, status=status.HTTP_200_OK)
