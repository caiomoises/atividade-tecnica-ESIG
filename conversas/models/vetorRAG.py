from django.db import models
from .documentos import Documento
from pgvector.django import VectorField

class VetorDocumento(models.Model):
    page_content = models.TextField(
        'Conteúdo da página',
        help_text="Conteúdo da página",
        null=True,
        blank=True,
    )

    documento = models.ForeignKey(
        Documento,
        on_delete=models.CASCADE,
        related_name='vetores'
    )

    embedding = VectorField(
        dimensions=1536
    )

    metadata = models.JSONField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Vetor do documento {self.documento.nome}"
