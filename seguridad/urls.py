from django.urls import path, re_path, include
from seguridad.views import Login
from django.contrib.auth.views import LogoutView
from web import views

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
    path('index/api/changePass', views.changePass)
]