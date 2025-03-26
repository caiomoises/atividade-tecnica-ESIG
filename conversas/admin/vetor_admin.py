from django.contrib import admin
from ..models import VetorDocumento

admin.site.register(VetorDocumento)
class VetorDocumentoAdmin(admin.ModelAdmin):
    list_display = ('documento', 'embedding')
    search_fields = ('documento', 'embedding')
    list_filter = ('documento', 'embedding')
    ordering = ('documento', 'embedding')