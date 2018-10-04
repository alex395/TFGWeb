from django import forms
from .models import Noticia
from .models import Aviso
from .models import Cliente, Envio

class NoticiaForm(forms.ModelForm):

    class Meta:
     model = Noticia
     fields = ('titulo', 'descripcion', 'tipoNotificacion', 'imagen')

class AvisoForm(forms.ModelForm):

     class Meta:
      model = Aviso
      fields = ('titulo', 'descripcion', 'prioridad')

class EnvioForm(forms.ModelForm):

     class Meta:
      model = Envio
      fields = ('titulo', 'archivo')

class ClienteForm(forms.ModelForm):

     class Meta:
      model = Cliente
      fields = ()
