# Generated by Django 2.1.2 on 2018-10-30 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20181030_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='peticion',
            name='fechaEnvio',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='peticion',
            name='fechaLimite',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
