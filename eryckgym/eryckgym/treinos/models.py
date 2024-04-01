from django.db import models

class Exercicio(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=500)
    em_equipamento = models.BooleanField(default=True)
    idade_minima_aluno = models.PositiveIntegerField(default=12)

    def __str__(self):
            return f'Nome: {self.nome} | Descrição: {self.descricao} | Equipamento: {self.em_equipamento} | Idade Mínima: {self.idade_minima_aluno}'

class Treino(models.Model):
    nome = models.CharField(max_length=100)
    exercicios = models.ManyToManyField(Exercicio, through='Item')

    def __str__(self):
            return f'Nome: {self.nome} | Exercicio: {self.exercicios}'

class Item(models.Model):
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)

   