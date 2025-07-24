from rest_framework import viewsets
from ..models import Conversa
from ..serializers import ConversaSerializer

class ConversaViewSet(viewsets.ModelViewSet):
    queryset = Conversa.objects.all().order_by('-criado_em')
    serializer_class = ConversaSerializer