# Generated by Django 5.0.2 on 2024-02-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_titulo_data_exata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clube',
            name='ano_fundacao',
            field=models.PositiveIntegerField(default=1900),
        ),
    ]