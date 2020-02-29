from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.registrarse, name = 'registrarse'),
    path('login/', views.ingresar),
    

    
    
]