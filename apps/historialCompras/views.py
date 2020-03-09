from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioSala
import datetime

from apps.modelo.models import Sala, Persona, Horario, Boleto, Pelicula

def verHistorial(request):
    idp = request.user.persona_id
    
    
    listaBoletos = Boleto.objects.filter(persona_id = idp)
    

    context = {
        'listaBoletos': listaBoletos,
        
    }
    return render(request,'historialcompras/historial_compras.html', context)

  

   
