from django.db import models
from .documentos import Documento
from pgvector.django import VectorField

class VetorDocumento(models.Model):
    documento = models.ForeignKey(
        Documento,
        on_delete=models.CASCADE,
        related_name='vetores'
    )

    embedding = VectorField(
        dimensions=1536
    )
