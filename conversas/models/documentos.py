from django.db import models

class Documento(models.Model):
    nome = models.CharField(
        'Nome',
        max_length=255,
        help_text="Nome do documento"
    )
    
    arquivo = models.FileField(
        'Arquivo',
        upload_to='documentos/',
        help_text="Arquivo do documento"
    )

    criado_em = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )

    def __str__(self):
        return self.nome
    
    class Meta:
        app_label = 'conversas'
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
