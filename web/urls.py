from . import views
from django.urls import path

urlpatterns = [
        path('', views.index),
        path('noticia/list', views.noticiaList),
    ]
