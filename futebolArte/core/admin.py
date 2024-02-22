from django.contrib import admin
from .models import Clube, Jogador, Competicao, Titulo, Pais, Estado, Cidade
from django.utils.html import format_html

# Register your models here.
admin.site.register(Clube)
admin.site.register(Jogador)
admin.site.register(Competicao)
admin.site.register(Titulo)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)

list_display = ['image_tag']