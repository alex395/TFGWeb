from django import forms
from django.forms import ModelChoiceField
from .models import Noticia
from .models import Aviso
from .models import Cliente, Envio, Peticion

class NoticiaForm(forms.ModelForm):

    class Meta:
     model = Noticia
     fields = ('titulo', 'descripcion', 'tipoNotificacion', 'imagen')

class AvisoForm(forms.ModelForm):

     class Meta:
      model = Aviso
      fields = ('titulo', 'descripcion', 'prioridad')

class ClienteModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.nombre,obj.apellidos)

class EnvioForm(forms.ModelForm):
     cliente = ClienteModelChoiceField(queryset=Cliente.objects.all())
     class Meta:
      model = Envio
      fields = ('titulo', 'archivo', 'cliente')

class PeticionForm(forms.ModelForm):
     cliente = ClienteModelChoiceField(queryset=Cliente.objects.all())
     class Meta:
      model = Peticion
      fields = ('titulo', 'descripcion', 'fechaLimite','cliente')

class ClienteForm(forms.ModelForm):

     class Meta:
      model = Cliente
      fields = ()
