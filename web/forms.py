from django import forms
from django.forms import ModelChoiceField
from .models import Noticia
from .models import Aviso
from .models import Usuario, Recibo, Peticion, Noticias_usuarios, Envio
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
import datetime

class MailForm(forms.Form):
    asunto=forms.CharField(required=True)
    contenido=forms.CharField(max_length=999, widget=forms.Textarea)

class NoticiaForm(forms.ModelForm):

    class Meta:
     model = Noticia
     fields = ('titulo', 'descripcion', 'tipoNotificacion', 'foto')

class AvisoForm(forms.ModelForm):
     fechaLimite = forms.DateField(widget=SelectDateWidget, initial=timezone.now())
     def clean_date(self):
        fechaLimite = self.cleaned_data['fechaLimite']
        if fechaLimite < datetime.date.today():
            raise forms.ValidationError("La fecha límite no puede estar en pasado")
        return fechaLimite
     class Meta:
      model = Aviso
      fields = ('titulo', 'descripcion', 'fechaLimite', 'prioridad')

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
      fields = ('nombre','apellidos','email','telefono','direccion')

class EnvioForm(forms.ModelForm):

     class Meta:
      model = Envio
      fields = ()

class Noticias_usuariosForm(forms.ModelForm):

     class Meta:
         model = Noticias_usuarios
         fields = ()

