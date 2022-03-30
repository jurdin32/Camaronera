# Generated by Django 4.0.3 on 2022-03-26 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0002_empresa_actividad_empresa_direccion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piscina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=1)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('dimension', models.DecimalField(decimal_places=4, max_digits=9)),
                ('precria', models.BooleanField(default=True)),
                ('estado', models.BooleanField(default=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.empresa')),
            ],
        ),
    ]
