from django.shortcuts import render
#Importamos la vista genérica FormView
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
#Importamos el formulario de autenticación de django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import CustomAuthForm

# Create your views here.
class Login(FormView):
    #Establecemos la plantilla a utilizar
    template_name = 'login.html'
    #Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = CustomAuthForm
    #Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
    success_url =  reverse_lazy("web:index")

    def dispatch(self, request, *args, **kwargs):
        #Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        #Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)