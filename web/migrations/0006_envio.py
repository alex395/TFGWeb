# Generated by Django 2.1.1 on 2018-10-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('archivo', models.FileField(upload_to='archivos')),
                ('email', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=600)),
            ],
        ),
    ]
