from . import views
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
#En este archivo se encuentran todas las redirecciones del componente 'web'.
urlpatterns = [
        path('index/', login_required(views.index), name='index'),
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
        path('index/api/changePass', views.changePass),
        path('index/api/createEnvio', views.createEnvioApi),
        re_path(r'^envio/(?P<path>.+)/envioDescargar/$', login_required(views.envioDescargar), name='envioDescargar'),
        path(r'^aviso/(?P<pk>[0-9]+)/edit/$', login_required(views.avisoEditar), name='avisoEditar'),
        path(r'^noticia/(?P<pk>[0-9]+)/edit/$', login_required(views.noticiaEditar), name='noticiaEditar'),
        path(r'^usuario/(?P<pk>[0-9]+)/edit/$', login_required(views.usuarioEditar), name='usuarioEditar'),
        path(r'^usuario/(?P<pk>[0-9]+)/delete/$', login_required(views.removeUsuario), name='removeUsuario'),
        path(r'^peticion/(?P<pk>[0-9]+)/edit/$', login_required(views.peticionEditar), name='peticionEditar'),
        path(r'^peticion/list/$', login_required(views.peticionFiltrar), name='peticionFiltrar'),
        path(r'^usuario/(?P<destino>.+)/mail/$', login_required(views.post), name='post'),


    ]
