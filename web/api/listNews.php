from .models import Noticia
from django.utils import timezone
import json

noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
json.dumps(list)