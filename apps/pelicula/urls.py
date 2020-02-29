from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.principal, name = 'cine'),
    path('registrar_pelicula/', views.registrarPelicula),
    path('ver_pelicula/', views.verPelicula),
    path('editar_pelicula/', views.editarPelicula),
    path('ver_sala/', views.verSala),
    
]