from .services import gerar_e_salvar_embedding
from ..serializers import DocumentoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .services import extrair_texto
from ..models import Documento
from rest_framework import viewsets
import logging
from django.shortcuts import get_object_or_404
from django.http import FileResponse

logger = logging.getLogger(__name__)

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    def create(self, request, *args, **kwargs):
        arquivo = request.FILES.get("arquivo")
        print(f'Arquivo recebido: {arquivo}')
        if not arquivo:
            return Response({"error": "Arquivo não enviado"}, status=status.HTTP_400_BAD_REQUEST)
        
        if arquivo.size == 0:
            return Response({"error": "Arquivo vazio"}, status=status.HTTP_400_BAD_REQUEST)

        texto = extrair_texto(arquivo)
        documento = Documento.objects.create(nome=arquivo.name, arquivo=arquivo)
        # TODO: Gerar embeddings e salvar no PostgreSQL

        gerar_e_salvar_embedding(texto, documento)
        return Response({"message": "Arquivo processado com sucesso", "texto": texto}, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        documento = get_object_or_404(Documento.objects.all().first(), pk=pk)
        response = FileResponse(documento.arquivo)
        response['Content-Disposition'] = f'attachment; filename="{documento.nome}"'
        return response

    @action(detail=False, methods=['get'])
    def listar(self, request):
        documentos = Documento.objects.all()
        serializer = self.get_serializer(documentos, many=True)
        return Response(serializer.data)
