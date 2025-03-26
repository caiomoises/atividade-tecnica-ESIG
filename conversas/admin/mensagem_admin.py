from django.contrib import admin
from ..models import Mensagem

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'conversa',
        'texto',
        'resposta',
    )

    search_fields = (
        'conversa',
    )

    date_hierarchy = 'criado_em'
    
    list_filter = (
        'criado_em',
    )
    
    readonly_fields = (
        'criado_em',
    )