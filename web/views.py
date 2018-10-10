from .models import Noticia
from .forms import NoticiaForm
from .models import Aviso, Cliente, Envio, Peticion
from .forms import AvisoForm, ClienteForm, EnvioForm, PeticionForm
from django.utils import timezone
import xlrd
import os
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def index(request):
        return render(request, 'index/index.html', {})

def noticiaList(request):
        noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
        return render(request, 'noticia/list.html', {'noticias': noticias})

def noticiaEdit(request):
        if request.method == "POST":
            form = NoticiaForm(request.POST)
            if form.is_valid():
                noticia = form.save(commit=False)
                noticia.fecha = timezone.now()
                noticia.save()
                return redirect('/')
        else:
            form = NoticiaForm()
        return render(request, 'noticia/edit.html', {'form': form})

def avisoList(request):
        avisos = Aviso.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
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
      Cliente.objects.all().delete()
      for r in range(3, sheet.nrows):
          form = ClienteForm(request.POST)
          cliente = form.save(commit=False)
          nombre = sheet.cell(r,0).value
          apellidos = sheet.cell(r,1).value
          email = sheet.cell(r,2).value
          telefono = sheet.cell(r,3).value
          direccion = sheet.cell(r,4).value
          cliente.nombre = nombre
          cliente.apellidos = apellidos
          cliente.email = email
          cliente.telefono = telefono
          cliente.direccion = direccion
          cliente.save()
    return redirect('/')

def envioList(request):
        envios = Envio.objects.all()
        return render(request, 'envio/list.html', {'envios': envios})

def envioEdit(request):
        if request.method == "POST":
            form = EnvioForm(request.POST, request.FILES)
            if form.is_valid():
                envio = form.save(commit=False)
                envio.save()
                return redirect('/')
        else:
            form = EnvioForm()
        return render(request, 'envio/edit.html', {'form': form})

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
