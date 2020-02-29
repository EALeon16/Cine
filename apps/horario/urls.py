from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.listarHorarios, name = 'cartelera'),
    path('agregar_horarios/', views.agregarHorario1),

    
    
]

