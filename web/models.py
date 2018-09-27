from django.db import models
from django.utils import timezone
# Create your models here.
class Noticia(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    tipoNotificacion = models.TextField()

def publish(self):
    self.fecha = timezone.now()
    self.save()

def __str__(self):
    return self.title
