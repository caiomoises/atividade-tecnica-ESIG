from django.db import models

class Conversa(models.Model):
    usuario = models.CharField(
        'Usuário',
        max_length=255,
        help_text="Nome do usuário"
    )

    criado_em = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )

    def __str__(self):
        return f"Conversa de {self.usuario} em {self.criado_em}"
    
    class Meta:
        app_label = 'conversas'
        verbose_name = 'Conversa'
        verbose_name_plural = 'Conversas'