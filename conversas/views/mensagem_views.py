from rest_framework import viewsets
from ..models import Mensagem, Conversa
from ..serializers import MensagemSerializer
import re
import datetime


def gerar_titulo_automatico(texto):
    texto_limpo = re.sub(r'[^\w\s]', '', texto).strip()
    palavras = texto_limpo.split()
    if not palavras:
        return "Conversa sem título"
    titulo = ' '.join(palavras[:5])
    return titulo.capitalize()

class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all().order_by('criado_em')
    serializer_class = MensagemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        conversa_id = self.request.query_params.get('conversa', None)

        if conversa_id is not None:
            queryset = queryset.filter(conversa_id=conversa_id)

            # Verifica se é a primeira mensagem da conversa
            conversa = Conversa.objects.filter(id=conversa_id).first()
            if conversa:
                primeira_mensagem = queryset.order_by('criado_em').first()
                if primeira_mensagem:
                    titulo = gerar_titulo_automatico(primeira_mensagem.texto)
                    conversa.usuario = titulo
                    conversa.criado_em = primeira_mensagem.criado_em.strftime('%Y-%m-%d %H:%M:%S')
                    conversa.save()

        return queryset
