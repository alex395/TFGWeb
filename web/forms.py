from django import forms
from django.forms import ModelChoiceField
from .models import Noticia
from .models import Aviso
from .models import Usuario, Recibo, Peticion, Noticias_usuarios, Envio

class NoticiaForm(forms.ModelForm):

    class Meta:
     model = Noticia
     fields = ('titulo', 'descripcion', 'tipoNotificacion', 'foto')

class AvisoForm(forms.ModelForm):

     class Meta:
      model = Aviso
      fields = ('titulo', 'descripcion', 'prioridad')

class UsuarioModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.nombre,obj.apellidos)

class ReciboForm(forms.ModelForm):
     usuario = UsuarioModelChoiceField(queryset=Usuario.objects.all())
     class Meta:
      model = Recibo
      fields = ('titulo', 'pdf', 'usuario')

class PeticionForm(forms.ModelForm):
     usuario = UsuarioModelChoiceField(queryset=Usuario.objects.all())
     class Meta:
      model = Peticion
      fields = ('titulo', 'descripcion', 'fechaLimite','usuario')

class UsuarioForm(forms.ModelForm):

     class Meta:
      model = Usuario
      fields = ()

class UsuarioForm(forms.ModelForm):

     class Meta:
      model = Usuario
      fields = ()

class EnvioForm(forms.ModelForm):

     class Meta:
      model = Envio
      fields = ()

class Noticias_usuariosForm(forms.ModelForm):

     class Meta:
         model = Noticias_usuarios
         fields = ()

