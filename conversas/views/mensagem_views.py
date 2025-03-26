from rest_framework import viewsets
from ..models import Mensagem
from ..serializers import MensagemSerializer

class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer