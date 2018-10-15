from .models import Noticia
from .forms import NoticiaForm
from .models import Aviso, Usuario, Recibo, Peticion, Noticias_usuarios, Envio
from .forms import AvisoForm, UsuarioForm, ReciboForm, PeticionForm, Noticias_usuariosForm, EnvioForm
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


# Create your views here.
def index(request):
        return render(request, 'index/index.html', {})

def listNews(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
         data = serializers.serialize('json', noticias)
         return HttpResponse(data, content_type='application/json')

def listAvisos(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         avisos = Aviso.objects.filter(fechaLimite__lte=timezone.now()).order_by('fechaLimite')
         data = serializers.serialize('json', avisos)
         return HttpResponse(data, content_type='application/json')

def addNew(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         form = Noticias_usuariosForm(request.POST)
         noticia_usuario = form.save(commit=False)
         noticia_usuario.usuario_id = request.GET['usuario_id']
         noticia_usuario.noticia_id = request.GET['noticia_id']
         noticia_usuario.save()
         return HttpResponse('')

def containsNews(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         noticias_usuarios = Noticias_usuarios.objects.filter(usuario_id=request.GET['usuario_id'])
         data = serializers.serialize('json', noticias_usuarios)
         return HttpResponse(data, content_type='application/json')

def noticiasUsuarios(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         noticias_usuarios = Noticias_usuarios.objects.all()
         data = serializers.serialize('json', noticias_usuarios)
         return HttpResponse(data, content_type='application/json')

def myNews(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         noticias = Noticia.objects.raw('SELECT * FROM web_noticia INNER JOIN web_noticias_usuarios ON web_noticia.id=web_noticias_usuarios.noticia_id where web_noticias_usuarios.usuario_id='+request.GET['usuario_id'])
         data = serializers.serialize('json', noticias)
         return HttpResponse(data, content_type='application/json')


def createEnvio(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         avisos = Aviso.objects.filter(fechaLimite__lte=timezone.now()).order_by('fechaLimite')
         data = serializers.serialize('json', avisos)
         return HttpResponse(data, content_type='application/json')

def displayUser(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         users = Usuario.objects.filter(id=request.GET['usuario_id'])
         data = serializers.serialize('json', users)
         return HttpResponse(data, content_type='application/json')

def getUser(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         user = Usuario.objects.filter(Q(email=request.GET['email']) & Q(password=request.GET['password']))
         data = serializers.serialize('json', user)
         return HttpResponse(data, content_type='application/json')

def myEnvios(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         envios = Envio.objects.filter(usuario_id=request.GET['user_id'])
         data = serializers.serialize('json', envios)
         return HttpResponse(data, content_type='application/json')

def myPeticiones(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         peticiones = Peticion.objects.filter(usuario_id=request.GET['user_id'])
         data = serializers.serialize('json', peticiones)
         return HttpResponse(data, content_type='application/json')

def myRecibos(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         recibos = Recibo.objects.filter(usuario_id=request.GET['user_id'])
         data = serializers.serialize('json', recibos)
         return HttpResponse(data, content_type='application/json')

def removeNew(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         Noticias_usuarios.objects.filter(Q(noticia_id=request.GET['noticia_id']) & Q(usuario_id=request.GET['usuario_id'])).delete()
         return HttpResponse('')

def createEnvioApi(request):
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         form = EnvioForm(request.POST)
         envio = form.save(commit=False)
         envio.usuario_id = request.GET['usuario_id']
         envio.peticion_id = request.GET['peticion_id']
         envio.titulo = request.GET['titulo']
         envio.archivo = request.GET['archivo']
         envio.fecha = request.GET['fecha']
         envio.save()
         return HttpResponse('')

def noticiaList(request):
        noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
        return render(request, 'noticia/list.html', {'noticias': noticias})

def noticiaEdit(request):
        if request.method == "POST":
            form = NoticiaForm(request.POST, request.FILES)
            if form.is_valid():
                noticia = form.save(commit=False)
                noticia.fecha = timezone.now()
                noticia.save()
                return redirect('/')
        else:
            form = NoticiaForm()
        return render(request, 'noticia/edit.html', {'form': form})

def avisoList(request):
        avisos = Aviso.objects.filter(fecha__lte=timezone.now()).order_by('fechaLimite')
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
