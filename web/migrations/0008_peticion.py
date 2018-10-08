# Generated by Django 2.1.1 on 2018-10-08 11:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20181007_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peticion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('fechaEnvio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaLimite', models.DateTimeField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Cliente')),
            ],
        ),
    ]