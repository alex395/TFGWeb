from .models import Noticia
from django.utils import timezone
import json

print ("Access-Control-Allow-Origin:\n*")
print ("Access-Control-Allow-Headers:\n")
print ("Access-Control-Allow-Methods: GET, POST, OPTIONS\n")

noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
json.dumps(list)