from django import forms
from .models import Noticia
from .models import Aviso
from .models import Cliente

class NoticiaForm(forms.ModelForm):

    class Meta:
     model = Noticia
     fields = ('titulo', 'descripcion', 'tipoNotificacion', 'imagen')

class AvisoForm(forms.ModelForm):

     class Meta:
      model = Aviso
      fields = ('titulo', 'descripcion', 'prioridad')

class ClienteForm(forms.ModelForm):

     class Meta:
      model = Cliente
      fields = ()
