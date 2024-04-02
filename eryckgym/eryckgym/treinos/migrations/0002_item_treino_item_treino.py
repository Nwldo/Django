# Generated by Django 5.0.3 on 2024-04-01 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treinos.exercicio')),
            ],
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('exercicios', models.ManyToManyField(through='treinos.Item', to='treinos.exercicio')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='treino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treinos.treino'),
        ),
    ]