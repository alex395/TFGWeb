from django.db import models
from django.utils import timezone
# Create your models here.
class Noticia(models.Model):
    EMAIL = 'Email'
    TELEFONO = 'Telefono'
    AMBOS = 'Ambos'
    NINGUNO = 'NINGUNO'
    notificacion_choices = ((EMAIL, 'Email'),
    (TELEFONO, 'Telefono'),
    (AMBOS, 'Ambos'),
    (NINGUNO, 'Ninguno'),)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.TextField(blank=True)
    fecha = models.DateTimeField(default=timezone.now)
    tipoNotificacion = models.TextField(choices=notificacion_choices, default = AMBOS)

class Aviso(models.Model):
    BAJO = 'Bajo'
    MEDIO = 'Medio'
    ALTO = 'Alto'
    prioridad_choices = ((BAJO, 'Bajo'),
    (MEDIO, 'Medio'),
    (ALTO, 'Alto'),)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    prioridad = models.TextField(choices=prioridad_choices, default = MEDIO)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=600)

class Envio(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='archivos')

def __str__(self):
    return self.title
