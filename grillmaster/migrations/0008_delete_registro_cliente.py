# Generated by Django 5.0.6 on 2024-06-13 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grillmaster', '0007_remove_registro_cliente_cliente_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registro_cliente',
        ),
    ]