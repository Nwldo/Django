# Generated by Django 5.0.2 on 2024-02-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_titulo_ano_conquista_alter_titulo_data_exata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo',
            name='data_exata',
            field=models.DateField(),
        ),
    ]
