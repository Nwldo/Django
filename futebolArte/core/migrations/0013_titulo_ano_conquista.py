# Generated by Django 5.0.2 on 2024-02-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_titulo_ano_conquista'),
    ]

    operations = [
        migrations.AddField(
            model_name='titulo',
            name='ano_conquista',
            field=models.PositiveIntegerField(default=1970),
        ),
    ]
