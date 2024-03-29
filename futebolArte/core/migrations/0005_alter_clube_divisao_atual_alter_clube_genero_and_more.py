# Generated by Django 5.0.2 on 2024-02-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_clube_divisao_atual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clube',
            name='divisao_atual',
            field=models.CharField(choices=[('A', 'Série A'), ('B', 'Série B'), ('C', 'Série C'), ('D', 'Série D'), ('A', 'Série A')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='clube',
            name='genero',
            field=models.CharField(choices=[('MA', 'MASCULINO'), ('FE', 'FEMININO')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='sexo',
            field=models.CharField(choices=[('MA', 'MASCULINO'), ('FE', 'FEMININO')], default='', max_length=50),
        ),
    ]
