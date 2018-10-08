from . import views
from django.urls import path, re_path

urlpatterns = [
        path('', views.index),
        path('noticia/list', views.noticiaList),
        path('noticia/edit', views.noticiaEdit),
        path('aviso/list', views.avisoList),
        path('aviso/edit', views.avisoEdit),
        path('excel/actualizar', views.excelActualizar),
        path('envio/list', views.envioList),
        path('envio/edit', views.envioEdit),
        path('peticion/list', views.peticionList),
        path('peticion/edit', views.peticionEdit),
        re_path(r'^envio/(?P<path>.+)/envioDescargar/$', views.envioDescargar, name='envioDescargar'),
        path(r'^aviso/(?P<pk>[0-9]+)/edit/$', views.avisoEditar, name='avisoEditar'),
        path(r'^noticia/(?P<pk>[0-9]+)/edit/$', views.noticiaEditar, name='noticiaEditar'),
        path(r'^peticion/(?P<pk>[0-9]+)/edit/$', views.peticionEditar, name='peticionEditar'),

    ]
