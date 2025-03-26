from rest_framework import viewsets
from ..models import Conversa
from ..serializers import ConversaSerializer

class ConversaViewSet(viewsets.ModelViewSet):
    queryset = Conversa.objects.all()
    serializer_class = ConversaSerializer