# Generated by Django 2.1.2 on 2018-10-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_noticia_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='url',
            field=models.URLField(default='/', max_length=400),
            preserve_default=False,
        ),
    ]
