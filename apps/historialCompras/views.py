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

def pdfBoleto(request):
    bol = request.GET.get('nro')
    now = datetime.date.today()
    
    print(now)
    listaFactura = Boleto.objects.filter(boleto_id = bol)
    suma = listaFactura.values_list('cantidad_boletoN', flat=True).first()
    mul = suma * 7;
    suma2 = listaFactura.values_list('cantidad_boletoE', flat=True).first()
    mul2 = suma2 * 3.5
    context = {
        'listaF': listaFactura,
        'f': now,
        'mul': mul,
        'mul2': mul2,
    }
    
    return render(request,'boleto/pdf.html', context)    

   
