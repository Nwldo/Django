from django.db import models
from treinos.models import Treino

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)
    treino = models.OneToOneField(Treino, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
            return f'Nome: {self.nome} | Idade: {self.idade} | Treino {self.treino}'

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = age = models.CharField(max_length=100)
    treinos = models.ManyToManyField(Treino)

    def __str__(self):
            return f'Nome: {self.nome} | Especialidade: {self.especialidade} | Treino {self.treinos}'