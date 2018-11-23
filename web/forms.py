from django import forms
from django.forms import ModelChoiceField
from .models import Noticia
from .models import Aviso
from .models import Usuario, Recibo, Peticion, Noticias_usuarios, Envio
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
import datetime
from django.forms import DateField

#Estos son los diferentes formularios que usaremos en nuestra aplicación.


#Formulario para enviar email.
class MailForm(forms.Form):
    asunto=forms.CharField(required=True)
    contenido=forms.CharField(max_length=999, widget=forms.Textarea)

#Formulario para crear noticia.

class NoticiaForm(forms.ModelForm):
    class Meta:
     model = Noticia
     fields = ('titulo', 'descripcion', 'url', 'foto')

#Formulario para crear un aviso.
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

#Modificador del campo en el que se muestra un usuario relacionado para que solo muestre su nombre y apellidos.
class UsuarioModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.nombre,obj.apellidos)

#Formulario de creación de un recibo.
class ReciboForm(forms.ModelForm):
     usuario = UsuarioModelChoiceField(queryset=Usuario.objects.all())
     class Meta:
      model = Recibo
      fields = ('titulo', 'pdf', 'usuario')

#Formulario de creación de una petición.
class PeticionForm(forms.ModelForm):
    usuario = UsuarioModelChoiceField(queryset=Usuario.objects.all())
    fechaLimite = forms.DateField(widget=SelectDateWidget, initial=timezone.now())
    def clean_date(self):
        fechaLimite = self.cleaned_data['fechaLimite']
        if fechaLimite < datetime.date.today():
            raise forms.ValidationError("La fecha límite no puede estar en pasado")
        return fechaLimite

    class Meta:
      model = Peticion
      fields = ('titulo', 'descripcion', 'fechaLimite','usuario')

#Formulario de creación de un usuario.
class UsuarioForm(forms.ModelForm):

     class Meta:
      model = Usuario
      fields = ('nombre','apellidos','email','telefono','direccion')

#Formulario de creación de un envío.
class EnvioForm(forms.ModelForm):

     class Meta:
      model = Envio
      fields = ()

#Tabla que relaciona a los usuarios con las noticias favoritas.
class Noticias_usuariosForm(forms.ModelForm):

     class Meta:
         model = Noticias_usuarios
         fields = ()

