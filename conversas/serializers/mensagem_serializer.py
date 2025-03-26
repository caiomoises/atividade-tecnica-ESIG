from rest_framework import serializers
from ..models import Mensagem

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = '__all__'
