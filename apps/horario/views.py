from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .forms import FormularioHorario, FormularioHorario
from apps.modelo.models import Horario, Pelicula, Sala


def agregarHorario(request):
    peli = request.GET['peli']
    pelicula = Pelicula.objects.get(pelicula_id = peli)
    lista = Pelicula.objects.all()
    listas= Sala.objects.all()
    formulario_horario = FormularioHorario(request.POST)
    if request.method == 'POST':
        if formulario_horario.is_valid():
            datos = formulario_horario.cleaned_data
            horario = Horario()
            horario.hora_pelicula = datos.get('hora_pelicula')
            horario.fecha_pelicua = datos.get('fecha_pelicua')
            horario.calidad_pelicula = datos.get('calidad_pelicula')
            horario.pelicula = pelicula
            horario.sala = datos.get('sala')
            horario.save()
            messages.success(request, 'Horario registrado correctamente')
            return redirect('/cartelera')
        else:
            messages.error(request, 'Esta pelicula ya esta registrada')
                 
   
    
    context = {
        'f': formulario_horario,
        'lista': lista,
        'listas': listas
    }
    
    return render(request,'horario/agregar_horario.html', context)


def agregarHorario1 (request):
    lista = Pelicula.objects.all()
    listas= Sala.objects.all()
    peli = request.GET.get('peli')
    peliculas = Pelicula.objects.get(pelicula_id = peli)
    formulario_horario = FormularioHorario(request.POST)
    if request.method == 'POST':
        if formulario_horario.is_valid():
            datos = formulario_horario.cleaned_data
            existes = (Horario.objects.filter(sala_id = datos.get('sala') , fecha_pelicua = datos.get('fecha_pelicua') ,hora_pelicula = datos.get('hora_pelicula')).count() > 0)
            existef = (Horario.objects.filter(fecha_pelicua = datos.get('fecha_pelicua')).count() > 0)
            existeh = (Horario.objects.filter(hora_pelicula = datos.get('hora_pelicula')).count() > 0)

            if existes:
                messages.error(request, 'Este horario ya esta registrado')
            else:
                horario = Horario()
                horario.hora_pelicula = datos.get('hora_pelicula')
                horario.fecha_pelicua = datos.get('fecha_pelicua')
                horario.pelicula = peliculas
                horario.sala = datos.get('sala')
                horario.save()
                messages.success(request, 'Horario registrado correctamente')
                return redirect('/cartelera')

    context = {
        'f': formulario_horario,
        'lista': lista,
        'listas': listas,
        'peliculas':peliculas
    }
    
    return render(request,'horario/agregar_horario.html', context)

def listarHorarios(request):
    lista = Horario.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'horario/listar_horarios.html', context)
        

def Search(request):
    queryset = request.GET.get("datepicker")
    listaB = Horario.objects.all()
    if queryset:
        listaB = Horario.objects.filter(
            Q(fecha_pelicua = queryset)

        ).distinct()
    return render('principal.html')    





