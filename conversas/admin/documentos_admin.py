from django.contrib import admin
from ..models import Documento

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'criado_em'
    )

    search_fields = (
        'nome',
    )

    date_hierarchy = 'criado_em'
    
    list_filter = (
        'criado_em',
    )
    
    readonly_fields = (
        'criado_em',
    )