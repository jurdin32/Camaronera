# Generated by Django 4.0.3 on 2022-03-24 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0002_alter_categoria_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.categoria')),
            ],
        ),
    ]