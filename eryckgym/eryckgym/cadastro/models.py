from django.db import models
from treinos.models import Treino

class Aluno(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )


    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='N')
    idade = models.IntegerField(default=0)
    cpf = models.CharField(max_length=11,default=0)
    telefone = models.CharField(max_length=14,default=0)
    treino = models.OneToOneField(Treino, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
            return f'Nome: {self.nome} | Sexo: {self.sexo} | Idade: {self.idade} | CPF: {self.cpf} | Telefone: {self.telefone} | Treino {self.treino}'

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    treinos = models.ManyToManyField(Treino, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
            return f'Nome: {self.nome} | Especialidade: {self.especialidade} | Treino {self.treinos}'