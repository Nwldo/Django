# Generated by Django 5.0.2 on 2024-02-22 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_competicao_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogador',
            options={'verbose_name': 'Jagador', 'verbose_name_plural': 'Jogadores'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'País', 'verbose_name_plural': 'Países'},
        ),
        migrations.AlterModelOptions(
            name='titulo',
            options={'verbose_name': 'Título', 'verbose_name_plural': 'Títulos'},
        ),
    ]
