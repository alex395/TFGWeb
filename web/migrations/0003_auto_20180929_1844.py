# Generated by Django 2.1.1 on 2018-09-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180929_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.TextField(),
        ),
    ]
