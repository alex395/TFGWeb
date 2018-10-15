from . import views
from django.urls import path, re_path

urlpatterns = [
        path('', views.index),
        path('noticia/list', views.noticiaList),
        path('noticia/edit', views.noticiaEdit),
        path('aviso/list', views.avisoList),
        path('aviso/edit', views.avisoEdit),
        path('excel/actualizar', views.excelActualizar),
        path('recibo/list', views.reciboList),
        path('recibo/edit', views.reciboEdit),
        path('peticion/list', views.peticionList),
        path('peticion/edit', views.peticionEdit),
        path('api/listNews', views.listNews),
        path('api/listAvisos', views.listAvisos),
        path('api/addNew', views.addNew),
        path('api/containsNews', views.containsNews),
        path('api/noticiasUsuarios', views.noticiasUsuarios),
        path('api/displayUser', views.displayUser),
        path('api/getUser', views.getUser),
        path('api/myNews', views.myNews),
        path('api/myEnvios', views.myEnvios),
        path('api/myPeticiones', views.myPeticiones),
        path('api/myRecibos', views.myRecibos),
        path('api/removeNew', views.removeNew),
        path('api/createEnvio', views.createEnvioApi),
        re_path(r'^envio/(?P<path>.+)/envioDescargar/$', views.envioDescargar, name='envioDescargar'),
        path(r'^aviso/(?P<pk>[0-9]+)/edit/$', views.avisoEditar, name='avisoEditar'),
        path(r'^noticia/(?P<pk>[0-9]+)/edit/$', views.noticiaEditar, name='noticiaEditar'),
        path(r'^peticion/(?P<pk>[0-9]+)/edit/$', views.peticionEditar, name='peticionEditar'),


    ]
