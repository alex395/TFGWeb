from .models import Noticia
from .forms import NoticiaForm
from .corsthttp import CORSRequestHandler
from .models import Aviso, Usuario, Recibo, Peticion, Noticias_usuarios, Envio
from .forms import AvisoForm, UsuarioForm, ReciboForm, PeticionForm, Noticias_usuariosForm, EnvioForm, MailForm
from django.utils import timezone
import xlrd
import os
import json
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from django.db.models import Q
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
from django.core.mail import EmailMessage
from random import choice
import base64
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
        return render(request, 'index/index.html', {})

#---------- API ----------
def listNews(request):
         print ("Access-Control-Allow-Origin:")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
         data = serializers.serialize('json', noticias)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

def listAvisos(request):
         print ("Access-Control-Allow-Origin:*")
         print ("Access-Control-Allow-Headers:")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS")
         avisos = Aviso.objects.filter(fechaLimite__lte=timezone.now()).order_by('fechaLimite')
         data = serializers.serialize('json', avisos)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

@csrf_exempt
def addNew(request):
         body_unicode = request.body.decode('utf-8')
         body = json.loads(body_unicode)
         form = Noticias_usuariosForm(request.POST)
         noticia_usuario = form.save(commit=False)
         noticia_usuario.usuario_id = body['usuario_id']
         noticia_usuario.noticia_id = body['noticia_id']
         noticia_usuario.save()
         response = HttpResponse('true', content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

def containsNews(request):
         noticias_usuarios = Noticias_usuarios.objects.filter(usuario_id=request.GET['usuario_id'])
         data = serializers.serialize('json', noticias_usuarios)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

def noticiasUsuarios(request):
         noticias_usuarios = Noticias_usuarios.objects.all()
         data = serializers.serialize('json', noticias_usuarios)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

def myNews(request):
         noticias = Noticia.objects.raw('SELECT * FROM web_noticia INNER JOIN web_noticias_usuarios ON web_noticia.id=web_noticias_usuarios.noticia_id where web_noticias_usuarios.usuario_id='+request.GET['usuario_id'])
         data = serializers.serialize('json', noticias)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response


def createEnvio(request):
         avisos = Aviso.objects.filter(fechaLimite__lte=timezone.now()).order_by('fechaLimite')
         data = serializers.serialize('json', avisos)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

def displayUser(request):
         users = Usuario.objects.filter(id=request.GET['usuario_id'])
         data = serializers.serialize('json', users)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

@csrf_exempt
def getUser(request):
         body_unicode = request.body.decode('utf-8')
         body = json.loads(body_unicode)
         user = Usuario.objects.filter(Q(email=body['email']) & Q(password=body['password']))
         data = serializers.serialize('json', user)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

@csrf_exempt
def changePass(request):
         body_unicode = request.body.decode('utf-8')
         body = json.loads(body_unicode)
         Usuario.objects.filter(id=body['usuario_id']).update(password=body['password'])
         user= Usuario.objects.filter(id=body['usuario_id'])
         data = serializers.serialize('json', user)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response


def myEnvios(request):
         envios = Envio.objects.filter(usuario_id=request.GET['user_id'])
         data = serializers.serialize('json', envios)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response


def myPeticiones(request):
         peticiones = Peticion.objects.filter(usuario_id=request.GET['user_id'])
         data = serializers.serialize('json', peticiones)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

def myRecibos(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         recibos = Recibo.objects.filter(usuario_id=request.GET['usuario_id'])
         data = serializers.serialize('json', recibos)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

@csrf_exempt
def removeNew(request):
         body_unicode = request.body.decode('utf-8')
         body = json.loads(body_unicode)
         Noticias_usuarios.objects.filter(Q(noticia_id=body['noticia_id']) & Q(usuario_id=body['usuario_id'])).delete()
         response = HttpResponse('true', content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

@csrf_exempt
def createEnvioApi(request):
         body_unicode = request.body.decode('utf-8')
         body = json.loads(body_unicode)
         format, imgstr = body['archivo'].split(';charset=utf-8;base64,')
         ext = body['extension']
         data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
         form = EnvioForm()
         envio = form.save(commit=False)
         envio.usuario_id = body['usuario_id']
         envio.peticion_id = body['peticion_id']
         envio.titulo = body['titulo']
         envio.archivo = data
         envio.fecha = timezone.now()
         envio.save()
         Peticion.objects.filter(id=body['peticion_id']).update(resuelto=True)
         response = HttpResponse('true', content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         response.__setitem__("Access-Control-Allow-Headers","*")
         response.__setitem__("Access-Control-Allow-Methods","GET, POST, OPTIONS")
         return response

#---------- API ----------

def noticiaList(request):
        noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
        return render(request, 'noticia/list.html', {'noticias': noticias})

def noticiaEdit(request):
        if request.method == "POST":
            form = NoticiaForm(request.POST, request.FILES)
            if form.is_valid():
                noticia = form.save(commit=False)
                noticia.fecha = timezone.now()
                noticia.url = request.build_absolute_uri()
                noticia.save()
                return redirect('/')
        else:
            form = NoticiaForm()
        return render(request, 'noticia/edit.html', {'form': form})

def post(request, destino):
        if request.method == "POST":
           form=MailForm(request.POST)
           if form.is_valid():
               email = EmailMessage(form.cleaned_data['asunto'], form.cleaned_data['contenido'], 'ardbudus@gmail.com', [destino])
               email.send()
               return HttpResponseRedirect('/')
        else:
           form = MailForm()
        return render(request,'usuario/mail.html',{'form':form})

def avisoList(request):
        avisos = Aviso.objects.filter(fechaLimite__lte=timezone.now()).order_by('fechaLimite')
        return render(request, 'aviso/list.html', {'avisos': avisos})

def avisoEdit(request):
        if request.method == "POST":
            form = AvisoForm(request.POST)
            if form.is_valid():
                    aviso = form.save(commit=False)
                    aviso.fecha = timezone.now()
                    aviso.save()
                    return redirect('/')
        else:
            form = AvisoForm()
        return render(request, 'aviso/edit.html', {'form': form})

def avisoEditar(request, pk):
        aviso = get_object_or_404(Aviso, pk=pk)
        if request.method == "POST":
            form = AvisoForm(request.POST, instance=aviso)
            if form.is_valid():
                aviso = form.save(commit=False)
                aviso.save()
                return redirect('/')
        else:
            form = AvisoForm(instance=aviso)
        return render(request, 'aviso/edit.html', {'form': form})

def noticiaEditar(request, pk):
        noticia = get_object_or_404(Noticia, pk=pk)
        if request.method == "POST":
            form = NoticiaForm(request.POST, instance=noticia)
            if form.is_valid():
                noticia = form.save(commit=False)
                noticia.save()
                return redirect('/')
        else:
            form = NoticiaForm(instance=noticia)
        return render(request, 'noticia/edit.html', {'form': form})

def excelActualizar(request):
    myfile = request.FILES['file']
    name = request.FILES['file'].name
    if name[-3:] == "xls" or name[-3:]== "xlsx":
      book = xlrd.open_workbook(file_contents=myfile.read())
      sheet = book.sheet_by_name("Sheet1")
      Usuario.objects.all().delete()
      for r in range(3, sheet.nrows):
          form = UsuarioForm(request.POST)
          usuario = form.save(commit=False)
          nombre = sheet.cell(r,0).value
          apellidos = sheet.cell(r,1).value
          email = sheet.cell(r,2).value
          telefono = sheet.cell(r,3).value
          direccion = sheet.cell(r,4).value
          usuario.nombre = nombre
          usuario.apellidos = apellidos
          usuario.email = email
          usuario.telefono = telefono
          usuario.direccion = direccion
          usuario.save()
    return redirect('/')

def reciboList(request):
        recibos = Recibo.objects.all()
        return render(request, 'recibo/list.html', {'recibos': recibos})

def reciboEdit(request):
        if request.method == "POST":
            form = ReciboForm(request.POST, request.FILES)
            if form.is_valid():
                recibo = form.save(commit=False)
                recibo.fecha = timezone.now()
                recibo.save()
                return redirect('/')
        else:
            form = ReciboForm()
        return render(request, 'recibo/edit.html', {'form': form})

def envioDescargar(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def peticionEdit(request):
        if request.method == "POST":
            form = PeticionForm(request.POST)
            if form.is_valid():
                peticion = form.save(commit=False)
                peticion.fechaEnvio = timezone.now()
                peticion.save()
                return redirect('/')
        else:
            form = PeticionForm()
        return render(request, 'peticion/edit.html', {'form': form})

def peticionList(request):
        peticiones = Peticion.objects.filter(fechaEnvio__lte=timezone.now()).order_by('fechaEnvio')
        return render(request, 'peticion/list.html', {'peticiones': peticiones})

def peticionEditar(request, pk):
        peticion = get_object_or_404(Peticion, pk=pk)
        if request.method == "POST":
            form = PeticionForm(request.POST, instance=peticion)
            if form.is_valid():
                peticion = form.save(commit=False)
                peticion.save()
                return redirect('/')
        else:
            form = PeticionForm(instance=peticion)
        return render(request, 'peticion/edit.html', {'form': form})

def usuarioEdit(request):
        if request.method == "POST":
            form = UsuarioForm(request.POST)
            if form.is_valid():
                    usuario = form.save(commit=False)
                    pwd = generarPass()
                    usuario.password = pwd
                    usuario.save()
                    email = EmailMessage('Bienvenido '+form.cleaned_data['nombre']+' a Asecon', 'Su contraseña para acceder al área cliente de nuestra app es '+pwd, 'ardbudus@gmail.com', [form.cleaned_data['email']])
                    email.send()
                    return redirect('/')
        else:
            form = UsuarioForm()
        return render(request, 'usuario/edit.html', {'form': form})


def generarPass():
         longitud = 8
         valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
         p = ""
         p = p.join([choice(valores) for i in range(longitud)])
         return p

def usuarioEditar(request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        if request.method == "POST":
            form = UsuarioForm(request.POST, instance=usuario)
            if form.is_valid():
                usuario = form.save(commit=False)
                usuario.save()
                return redirect('/')
        else:
            form = UsuarioForm(instance=usuario)
        return render(request, 'usuario/edit.html', {'form': form})


def usuarioList(request):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario/list.html', {'usuarios': usuarios})

def removeUsuario(request, pk):
         Usuario.objects.filter(id=pk).delete()
         return redirect('/')


