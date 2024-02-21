from django.db import models

# Create your models here. (base de dados)
ge = (
        ("MA","MASCULINO"),
        ("FE","FEMININO"),
    )

class Clube(models.Model):
    nome = models.CharField(max_length=120)
    ano_fundacao = models.DateField()
    # Divisão atual
    da = (
        ("A","Série A"),
        ("B","Série B"),
        ("C","Série C"),
        ("D","Série D"),
        ("A","Série A"),
    )
    divisao_atual= models.CharField(max_length=50,choices=da, default='')
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)
    genero = models.CharField(max_length=50,choices=ge, default='')

class Jogador(models.Model):
    nome = models.CharField(max_length=120)
    #foto = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='foto')
    posicao_principal = models.CharField(max_length=50)
    numero_camisa = models.IntegerField()
    sexo = models.CharField(max_length=50,choices=ge, default='')
    
    # relacionamento
    clube = models.ForeignKey(Clube, on_delete=models.SET_NULL, related_name='sem_clube', null=True)


class Competicao(models.Model):
    nome = models.CharField(max_length=120)
    # Tipos de disputas
    td = (
        ("ES", "ESTADUAL"),
        ("NA","NACIONAL"),
        ("IN","INTERNACIONAL"),
    )
    tipo_disputa = models.CharField(max_length=50, choices=td, default='ES')
    #categoria de campeonatos
    cc = (
        ("CA", "CAMPEONATO"),
        ("COPA", "COPA"),
    )
    categoria = models.CharField(max_length=50, choices=cc, default='CA')

    # relacionamento

class Titulo(models.Model):
    ano_conquista = models.DateField()
    data_exata = models.DateField()
    # resultado da competição
    result = (
        ("CAMP", "CAMPEÃO"),
        ("VICE", "VICE-CAMPEÃO"),
    )
    resultado = models.CharField(max_length=50, choices=result, default='CAM')
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    competicao = models.ForeignKey(Competicao,on_delete=models.CASCADE)
