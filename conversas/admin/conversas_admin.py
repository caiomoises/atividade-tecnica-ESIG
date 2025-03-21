from django.contrib import admin
from ..models import Conversa

@admin.register(Conversa)
class ConversaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'criado_em'
    )

    search_fields = (
        'usuario',
    )

    date_hierarchy = 'criado_em'
    
    list_filter = (
        'criado_em',
    )
    
    readonly_fields = (
        'criado_em',
    )