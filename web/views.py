from django.shortcuts import render
from .models import Noticia
from django.utils import timezone
# Create your views here.
def index(request):
        return render(request, 'index/index.html', {})

def noticiaList(request):
        noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
        return render(request, 'noticia/list.html', {'noticias': noticias})
