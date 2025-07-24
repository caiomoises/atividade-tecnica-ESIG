from django.db import models
from .conversas import Conversa

class Mensagem(models.Model):
    conversa = models.ForeignKey(
        Conversa,
        on_delete=models.CASCADE,
        related_name='mensagens'
    )

    texto = models.TextField(
        'Texto',
        help_text="Texto da mensagem"
    )
    
    resposta = models.TextField(
        'Resposta',
        help_text="Resposta da mensagem",
        blank=True,
        null=True,
    )

    documento = models.ForeignKey(
        'Documento',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='mensagens'
    )
    
    criado_em = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )

    erro = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"Mensagem {self.id} - {self.texto[:50]}"
    
    class Meta:
        app_label = 'conversas'
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
