# Generated by Django 4.0.3 on 2022-03-25 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0005_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='gramaje',
        ),
    ]