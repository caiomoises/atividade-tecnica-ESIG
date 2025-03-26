from rest_framework import serializers
from ..models import Conversa

class ConversaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversa
        fields = '__all__'
