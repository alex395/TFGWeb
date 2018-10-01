from . import views
from django.urls import path

urlpatterns = [
        path('', views.index),
        path('noticia/list', views.noticiaList),
        path('noticia/edit', views.noticiaEdit),
        path('aviso/list', views.avisoList),
        path('aviso/edit', views.avisoEdit),
        path('excel/actualizar', views.excelActualizar),
        path(r'^aviso/(?P<pk>[0-9]+)/edit/$', views.avisoEditar, name='avisoEditar'),
        path(r'^noticia/(?P<pk>[0-9]+)/edit/$', views.noticiaEditar, name='noticiaEditar'),
    ]
