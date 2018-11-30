from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


#Formulario de login.
class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Usuario'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Contraseña'}))