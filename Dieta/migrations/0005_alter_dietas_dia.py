# Generated by Django 4.0.3 on 2022-03-29 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dieta', '0004_alter_dias_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietas',
            name='dia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dieta.dias', unique=True),
        ),
    ]
