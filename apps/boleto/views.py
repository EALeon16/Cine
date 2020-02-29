from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  FormularioBoleto
from apps.modelo.models import Pelicula, Persona, Sala, Horario, Boleto

def vistaBoleto(request):
    horario = request.GET.get('id')
    cartelera = Horario.objects.get(horario_id = horario)
    formulario_boleto = FormularioBoleto(request.POST)
    if request.method == 'POST':
        if formulario_boleto.is_valid():
            datos = formulario_boleto.cleaned_data
            boleto = Boleto()
            boleto.cantidad_boletoN = datos.get('cntBolN')
            boleto.cantidad_boletoE = datos.get('cntBolE')
            boleto.precio_total = datos.get('precioTotal')
            boleto.precio_total = datos.get('cantidadTotal')
            boleto.persona = 1
            boleto.horario = cartelera
            boleto.save()
            messages.success(request, 'Horario registrado correctamente')
            return redirect('/cartelera')
        else:
            messages.error(request, 'Error')
            return redirect('/cartelera')
                 
   
    
    context = {
        'f': formulario_boleto
    }
    return render(request,'boleto/adquirir_boleto.html')

def agregarBoleto(request):
    
    
    return render(request,'horario/agregar_horario.html', context)
