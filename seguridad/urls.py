from django.urls import path, re_path, include
from seguridad.views import Login
from django.contrib.auth.views import LogoutView
from web import views
from django.contrib.auth.decorators import login_required

#Aquí tenemos todas las redirecciones de la API.
urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('salir/', LogoutView.as_view(template_name='logout.html'), name="salir"),
    path('index/api/listNews', views.listNews),
    path('index/api/listAvisos', views.listAvisos),
    path('index/api/addNew', views.addNew),
    path('index/api/containsNews', views.containsNews),
    path('index/api/noticiasUsuarios', views.noticiasUsuarios),
    path('index/api/displayUser', views.displayUser),
    path('index/api/getUser', views.getUser),
    path('index/api/myNews', views.myNews),
    path('index/api/myEnvios', views.myEnvios),
    path('index/api/myPeticiones', views.myPeticiones),
    path('index/api/myRecibos', views.myRecibos),
    path('index/api/removeNew', views.removeNew),
    path('index/api/createEnvio', views.createEnvioApi),
    path('index/api/changePass', views.changePass),
    path('index/api/sendPass', views.sendPass),
    path('index/aviso/list', login_required(views.avisoList)),
    path('index/noticia/list', login_required(views.noticiaList)),
    path('index/noticia/edit', login_required(views.noticiaEdit)),
    path('index/aviso/list', login_required(views.avisoList)),
    path('index/aviso/edit', login_required(views.avisoEdit)),
    path('index/excel/actualizar', login_required(views.excelActualizar)),
    path('index/recibo/list', login_required(views.reciboList)),
    path('index/recibo/edit', login_required(views.reciboEdit)),
    path('index/peticion/list', login_required(views.peticionList)),
    path('index/peticion/edit', login_required(views.peticionEdit)),
    path('index/usuario/list', login_required(views.usuarioList)),
    path('index/usuario/edit', login_required(views.usuarioEdit)),
]