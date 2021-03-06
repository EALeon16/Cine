"""Cine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.pelicula import views
from django.contrib.auth import logout



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cine/', include('apps.pelicula.urls')), 
    path('cartelera/', include('apps.horario.urls')),
    path('agregar_sala/', include('apps.sala.urls')),
    path('adquirirBoleto/', include('apps.boleto.urls')),
    path('registrarse/', include('apps.persona.urls')),
    path('login/', include('apps.login.urls')),
    path('logout/', include('apps.logout.urls')),
    path('historailCompras/', include('apps.historialCompras.urls')),
    path('pdfBoleto/', include('apps.pdf.urls')),
    
   
    
]

#PARA IMAGENES
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
