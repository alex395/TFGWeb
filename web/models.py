from django.db import models
from django.utils import timezone
from datetime import date
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# En este archivo están creados los diferentes modelos del sistema, definiendo sus atributos.


def no_past(value):
    today = date.today()
    if value < today:
        raise ValidationError('La fecha debe ser futura')

class Noticia(models.Model):
    EMAIL = 'Email'
    TELEFONO = 'Telefono'
    AMBOS = 'Ambos'
    NINGUNO = 'NINGUNO'
    notificacion_choices = ((EMAIL, 'Email'),
    (TELEFONO, 'Telefono'),
    (AMBOS, 'Ambos'),
    (NINGUNO, 'Ninguno'),)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    url = models.URLField(max_length=1000)
    foto = models.ImageField(upload_to='imagenes', null=True, blank=True)
    fecha = models.DateField(default=timezone.now)

class Aviso(models.Model):
    BAJO = 'Bajo'
    MEDIO = 'Medio'
    ALTO = 'Alto'
    prioridad_choices = ((BAJO, 'Bajo'),
    (MEDIO, 'Medio'),
    (ALTO, 'Alto'),)
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    fechaLimite = models.DateField(null=False, blank=False, validators=[no_past])
    prioridad = models.TextField(choices=prioridad_choices, default = MEDIO)

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de teléfono debe ser introducido con el siguiente formato: '999999999'. Se admiten hasta 15 dígitos.")
    telefono =  models.CharField(validators=[phone_regex], max_length=15, null=False, blank=False)
    direccion = models.CharField(max_length=600)
    password = models.CharField(max_length=200, null=True, blank=True)

class Peticion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fechaEnvio = models.DateField(default=timezone.now)
    fechaLimite = models.DateField(null=False, blank=False, validators=[no_past])
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)
    resuelto = models.BooleanField(default=False)


class Recibo(models.Model):
    titulo = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='archivos')
    fecha = models.DateField(default=timezone.now)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)

class Envio(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='archivos')
    fecha = models.DateField(default=timezone.now)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)
    peticion = models.ForeignKey ('Peticion', on_delete=models.CASCADE, null=True)

class Noticias_usuarios(models.Model):
    usuario_id = models.IntegerField(null=True)
    noticia_id = models.IntegerField(null=True)

def __str__(self):
    return self.title
