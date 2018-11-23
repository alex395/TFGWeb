# Views.py es el View dentro de la arquitectura Model-View-Template. Se encargará de recoger las diferentes peticiones y de lanzar una respuesta.

from .models import Noticia
from .forms import NoticiaForm
from .corsthttp import CORSRequestHandler
from .models import Aviso, Usuario, Recibo, Peticion, Noticias_usuarios, Envio
from .forms import AvisoForm, UsuarioForm, ReciboForm, PeticionForm, Noticias_usuariosForm, EnvioForm, MailForm
from django.utils import timezone
import xlrd
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
from django.template import RequestContext, loader

#Se encarga de renderizar la vista 'index.html'
def index(request):
        return render(request, 'index/index.html', {})

#---------- API ----------
#Lista de noticias.
@csrf_exempt
def listNews(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         print ("Access-Control-Allow-Origin:")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
         data = serializers.serialize('json', noticias)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Lista de avisos.
@csrf_exempt
def listAvisos(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         print ("Access-Control-Allow-Origin:*")
         print ("Access-Control-Allow-Headers:")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS")
         avisos = Aviso.objects.all()
         data = serializers.serialize('json', avisos)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Añade una noticia a la base de datos.
@csrf_exempt
def addNew(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         form = Noticias_usuariosForm(request.POST)
         noticia_usuario = form.save(commit=False)
         noticia_usuario.usuario_id = body['usuario_id']
         noticia_usuario.noticia_id = body['noticia_id']
         noticia_usuario.save()
         response = HttpResponse('true', content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Comprueba si el usuario tiene alguna noticia en favoritos.
@csrf_exempt
def containsNews(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         noticias_usuarios = Noticias_usuarios.objects.filter(usuario_id=body['usuario_id'])
         data = serializers.serialize('json', noticias_usuarios)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Devuelve la tabla completa que relaciona a los usuarios con sus noticias favoritas.
@csrf_exempt
def noticiasUsuarios(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         noticias_usuarios = Noticias_usuarios.objects.all()
         data = serializers.serialize('json', noticias_usuarios)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Selecciona las noticias favoritas de un usuario.
@csrf_exempt
def myNews(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         noticias = Noticia.objects.raw('SELECT * FROM web_noticia INNER JOIN web_noticias_usuarios ON web_noticia.id=web_noticias_usuarios.noticia_id where web_noticias_usuarios.usuario_id='+str(body['usuario_id']))
         data = serializers.serialize('json', noticias)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response


@csrf_exempt
def createEnvio(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         avisos = Aviso.objects.filter(fechaLimite__lte=timezone.now()).order_by('fechaLimite')
         data = serializers.serialize('json', avisos)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response


#Muestra los datos de un usuario.
@csrf_exempt
def displayUser(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('')
         users = Usuario.objects.filter(id=body['usuario_id'])
         data = serializers.serialize('json', users)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Obtiene un usuario de la base de datos a partir de su nombre de su email y su contraseña.
@csrf_exempt
def getUser(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         user = Usuario.objects.filter(Q(email=body['email']) & Q(password=body['password']))
         data = serializers.serialize('json', user)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Cambia la contraseña de un usuario
@csrf_exempt
def changePass(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         Usuario.objects.filter(id=body['usuario_id']).update(password=body['password'])
         user= Usuario.objects.filter(id=body['usuario_id'])
         data = serializers.serialize('json', user)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Envia por mail la contraseña a un usuario en caso de haberla olvidado.
@csrf_exempt
def sendPass(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')

         pwd = generarPass()
         Usuario.objects.filter(email=body['email']).update(password=pwd)
         user= Usuario.objects.filter(email=body['email'])[:1].get()
         user1 = Usuario.objects.filter(email=body['email'])
         email = EmailMessage('Recordatorio de contraseña', user.nombre+' su nueva contraseña es '+user.password+' recuerde que puede cambiarla en cualquier momento en nuestra app', 'ardbudus@gmail.com', [body['email']])
         email.send()
         data = serializers.serialize('json', user1)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Lista los envios realizados por un usuario.
@csrf_exempt
def myEnvios(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         envios = Envio.objects.filter(usuario_id=body['user_id'])
         data = serializers.serialize('json', envios)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Lista las peticiones de un usuario.
@csrf_exempt
def myPeticiones(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         peticiones = Peticion.objects.filter(Q(usuario_id=body['user_id']) & Q(resuelto=False ))
         data = serializers.serialize('json', peticiones)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Lista los recibos de un usuario.
@csrf_exempt
def myRecibos(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         print ("Access-Control-Allow-Origin:\n*")
         print ("Access-Control-Allow-Headers:\n")
         print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")
         recibos = Recibo.objects.filter(usuario_id=body['usuario_id'])
         data = serializers.serialize('json', recibos)
         response = HttpResponse(data, content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Borra una noticia.
@csrf_exempt
def removeNew(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
         Noticias_usuarios.objects.filter(Q(noticia_id=body['noticia_id']) & Q(usuario_id=body['usuario_id'])).delete()
         response = HttpResponse('true', content_type='application/json')
         response.__setitem__("Access-Control-Allow-Origin","*")
         return response

#Realiza un envío por parte de un cliente.
@csrf_exempt
def createEnvioApi(request):
         body_unicode = request.body.decode('utf-8')
         try:
            body = json.loads(body_unicode)
         except ValueError:
            return HttpResponse('No tiene acceso a este recurso')
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

#Lista de noticias.
def noticiaList(request):
        noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
        paginator = Paginator(noticias, 5)
        page = request.GET.get('page')

        try:
           items = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           items = paginator.page(1)
        except EmptyPage:
          # If page is out of range (e.g. 9999), deliver last page of results.
          items= paginator.page(paginator.num_pages)
        return render(request, 'noticia/list.html', {'items': items})

#Editar una noticia.
def noticiaEdit(request):
        if request.method == "POST":
            form = NoticiaForm(request.POST, request.FILES)
            if form.is_valid():
                noticia = form.save(commit=False)
                noticia.save()
                return redirect('/index/aviso/list')
        else:
            form = NoticiaForm()
        return render(request, 'noticia/edit.html', {'form': form})

#Envía un correo a un cliente.
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

#Listado de avisos.
def avisoList(request):
        avisos = Aviso.objects.all()
        paginator = Paginator(avisos, 5)
        page = request.GET.get('page')

        try:
           items = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           items = paginator.page(1)
        except EmptyPage:
          # If page is out of range (e.g. 9999), deliver last page of results.
          items= paginator.page(paginator.num_pages)

        return render(request, 'aviso/list.html', {'avisos': avisos, 'items':items})

#Crear un aviso.
def avisoEdit(request):
        if request.method == "POST":
            form = AvisoForm(request.POST)
            if form.is_valid():
                    aviso = form.save(commit=False)
                    aviso.save()
                    return redirect('/index/aviso/list')
        else:
            form = AvisoForm()
        return render(request, 'aviso/edit.html', {'form': form})

#Editar un aviso.
def avisoEditar(request, pk):
        aviso = get_object_or_404(Aviso, pk=pk)
        if request.method == "POST":
            form = AvisoForm(request.POST, instance=aviso)
            if form.is_valid():
                aviso = form.save(commit=False)
                aviso.save()
                return redirect('/index/aviso/list')
        else:
            form = AvisoForm(instance=aviso)
        return render(request, 'aviso/edit.html', {'form': form})

#Editar una noticia.
def noticiaEditar(request, pk):
        noticia = get_object_or_404(Noticia, pk=pk)
        if request.method == "POST":
            form = NoticiaForm(request.POST, instance=noticia)
            if form.is_valid():
                noticia = form.save(commit=False)
                noticia.save()
                return redirect('/index/noticia/list')
        else:
            form = NoticiaForm(instance=noticia)
        return render(request, 'noticia/edit.html', {'form': form})

#Lee un fichero excel y lo inyecta en la base de datos.
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

#Lista de recibos.
def reciboList(request):
        recibos = Recibo.objects.all()
        paginator = Paginator(recibos, 5)
        page = request.GET.get('page')

        try:
           items = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           items = paginator.page(1)
        except EmptyPage:
          # If page is out of range (e.g. 9999), deliver last page of results.
          items= paginator.page(paginator.num_pages)

        return render(request, 'recibo/list.html', {'items': items})

#Crear un recibo.
def reciboEdit(request):
        if request.method == "POST":
            form = ReciboForm(request.POST, request.FILES)
            if form.is_valid():
                recibo = form.save(commit=False)
                recibo.fecha = timezone.now()
                recibo.save()
                return redirect('/index/recibo/list')
        else:
            form = ReciboForm()
        return render(request, 'recibo/edit.html', {'form': form})

#Descarga un fichero que se encuentra en la base de datos a través de un request y una ruta..
def envioDescargar(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

#Crear petición.
def peticionEdit(request):
        if request.method == "POST":
            form = PeticionForm(request.POST)
            if form.is_valid():
                peticion = form.save(commit=False)
                peticion.fechaEnvio = timezone.now()
                peticion.save()
                return redirect('/index/peticion/list')
        else:
            form = PeticionForm()
        return render(request, 'peticion/edit.html', {'form': form})

#Lista de peticiones.
def peticionList(request):
        items = Peticion.objects.filter(fechaEnvio__lte=timezone.now()).order_by('fechaEnvio')
        envios = Envio.objects.all()
        paginator = Paginator(items, 5)
        page = request.GET.get('page')

        try:
           peticiones = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           peticiones = paginator.page(1)
        except EmptyPage:
          # If page is out of range (e.g. 9999), deliver last page of results.
          peticiones= paginator.page(paginator.num_pages)
        return render(request, 'peticion/list.html', {'peticiones': peticiones,'envios': envios})

#Buscador de usuarios en peticiones.
def peticionFiltrar(request):
        if 'usrname' not in request.session:
           nombreusr = request.POST['user_name']
           request.session['usrname'] = nombreusr
           request.session['yaTiene'] = True;
        else:
            if 'yaTiene' not in request.session:
               nombreusr = request.session['usrname']
            else:
               if 'user_name' not in request.POST:
                   nombreusr = request.session['usrname']
               else:
                   request.session['usrname'] = request.POST['user_name']
                   nombreusr = request.session['usrname']

        noEntrar=False
        if len(nombreusr.split())==2:
          usuario = Usuario.objects.filter(Q(nombre__icontains=nombreusr.split()[0])&Q(apellidos__icontains=nombreusr.split()[1])).first()
        if len(nombreusr.split())==1:
          usuario = Usuario.objects.filter(Q(nombre__icontains=nombreusr.split()[0]) | Q(apellidos__icontains=nombreusr.split()[0])).first()
        if len(nombreusr.split()) !=2 and len(nombreusr.split())!=1:
          usuario =None
        if nombreusr == "":
          usuario=None
          items = Peticion.objects.all()
          noEntrar = True

        if noEntrar is False:
          if usuario != None:
            items = Peticion.objects.filter(usuario_id=usuario.id)
          else:
            items=None
            peticiones = None

        envios = Envio.objects.all()
        if items is not None:
           paginator = Paginator(items, 5)
           page = request.GET.get('page')

           try:
              peticiones = paginator.page(page)
           except PageNotAnInteger:
              # If page is not an integer, deliver first page.
              peticiones = paginator.page(1)
           except EmptyPage:
             # If page is out of range (e.g. 9999), deliver last page of results.
            peticiones= paginator.page(paginator.num_pages)

        return render(request, 'peticion/list.html', {'peticiones': peticiones,'envios': envios})

#Editar petición.
def peticionEditar(request, pk):
        peticion = get_object_or_404(Peticion, pk=pk)
        if request.method == "POST":
            form = PeticionForm(request.POST, instance=peticion)
            if form.is_valid():
                peticion = form.save(commit=False)
                peticion.save()
                return redirect('/index/peticion/list')
        else:
            form = PeticionForm(instance=peticion)
        return render(request, 'peticion/edit.html', {'form': form})

#Crear usuario.
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
                    return redirect('/index/usuario/list')
        else:
            form = UsuarioForm()
        return render(request, 'usuario/edit.html', {'form': form})

#Genera una contraseña aleatoria de 8 caracteres.
def generarPass():
         longitud = 8
         valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
         p = ""
         p = p.join([choice(valores) for i in range(longitud)])
         return p

#Editar un usuario.
def usuarioEditar(request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        if request.method == "POST":
            form = UsuarioForm(request.POST, instance=usuario)
            if form.is_valid():
                usuario = form.save(commit=False)
                usuario.save()
                return redirect('/index/usuario/list')
        else:
            form = UsuarioForm(instance=usuario)
        return render(request, 'usuario/edit.html', {'form': form})

#Listar usuarios.
def usuarioList(request):
        usuarios = Usuario.objects.all()
        paginator = Paginator(usuarios, 10)
        page = request.GET.get('page')

        try:
           items = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           items = paginator.page(1)
        except EmptyPage:
          # If page is out of range (e.g. 9999), deliver last page of results.
          items= paginator.page(paginator.num_pages)
        return render(request, 'usuario/list.html', {'items': items})

#Eliminar usuarios.
def removeUsuario(request, pk):
         Usuario.objects.filter(id=pk).delete()
         return redirect('/index/usuario/list')


