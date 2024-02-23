# Generated by Django 5.0.2 on 2024-02-22 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_clube_divisao_atual_alter_clube_genero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('continente', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='clube',
            name='divisao_atual',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='clube',
            name='genero',
            field=models.CharField(choices=[('', ''), ('M', 'MASCULINO'), ('F', 'FEMININO')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='sexo',
            field=models.CharField(choices=[('', ''), ('M', 'MASCULINO'), ('F', 'FEMININO')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='clube',
            name='pais',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pais'),
        ),
    ]