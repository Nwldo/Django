# Generated by Django 5.0.2 on 2024-02-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_ano_clube_ano_fundacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clube',
            name='divisao_atual',
            field=models.CharField(max_length=50),
        ),
    ]
