from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.vistaBoleto, name = 'verBoleto'),
    path('agregar_boleto/', views.agregarBoleto),
    
]