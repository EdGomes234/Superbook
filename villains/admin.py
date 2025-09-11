# EDGAR GOMES OLIVEIRA

from django.contrib import admin
from .models import Villain

@admin.register(Villain)
# Register your models here.
class VillainAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'criado_em', 'email_contato']
    list_filter = ['cidade']
    search_fields = ['codinome', 'nome_real', 'cidade']

    fieldsets = (
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações Gerais', {
            'fields': ('poder_principal', 'cidade', 'historia')
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
    )
    
    readonly_fields = ['criado_em']

