from django.db import models

# Create your models here. (base de dados)
GENERO_CHOICES = (
        ("",""),
        ("M","MASCULINO"),
        ("F","FEMININO"),
    )

class Pais(models.Model):
    nome = models.CharField(max_length=50)
    continente = models.CharField(max_length=50)

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    regiao = models.CharField(max_length=50)

#relacioanamento
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    populacao = models.IntegerField()

    #relacioanamento
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Clube(models.Model):
    nome = models.CharField(max_length=100)
    ano_fundacao = models.DateField()
    divisao_atual= models.CharField(max_length=50,)
    genero = models.CharField(max_length=50,choices=GENERO_CHOICES, default='')

    #relacioanamento
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    #foto = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='foto')
    posicao_principal = models.CharField(max_length=50)
    numero_camisa = models.IntegerField()
    sexo = models.CharField(max_length=50,choices=GENERO_CHOICES, default='')
    
    # relacionamento
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    clube = models.ForeignKey(Clube, on_delete=models.SET_NULL, related_name='sem_clube', null=True)


class Competicao(models.Model):
    nome = models.CharField(max_length=100)
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
