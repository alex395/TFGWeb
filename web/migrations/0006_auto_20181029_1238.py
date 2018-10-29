# Generated by Django 2.1.2 on 2018-10-29 11:38

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20181026_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='peticion',
            name='resuelto',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='aviso',
            name='fechaLimite',
            field=models.DateTimeField(validators=[web.models.no_past]),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe ser introducido con el siguiente formato: '999999999'. Se admiten hasta 15 dígitos.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]