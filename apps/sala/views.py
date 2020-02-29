from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioSala
from apps.modelo.models import Sala

def agregarSala(request):
    formularioS = FormularioSala(request.POST)
    if request.method == 'POST':
        if formularioS.is_valid():
            datos = formularioS.cleaned_data
            sala = Sala()
            sala.nombre_sala = datos.get('nombre_sala')
            sala.nro_asientos = datos.get('nro_asientos')
            messages.success(request, 'Sala agregada correctamnete')
            sala.save()
            return redirect('/cine/ver_sala')
        else:
            messages.error(request, 'Esta sala ya existe')

    context = {
        'fs': formularioS,
    }
    return render(request,'salas/agregar_sala.html', context)
