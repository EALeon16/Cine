from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.verHistorial, name = 'verHistorial'),
    path('pdfBoleto/', views.pdfBoleto),
    
]