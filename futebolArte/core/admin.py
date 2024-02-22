from django.contrib import admin
from .models import Clube, Jogador, Competicao, Titulo

# Register your models here.
admin.site.register(Clube)
admin.site.register(Jogador)
admin.site.register(Competicao)
admin.site.register(Titulo)