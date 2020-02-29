from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioPelicula
from apps.modelo.models import Pelicula, Persona, Sala, Horario


def principal(request):
    lista = Horario.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'principal.html', context)



def registrarPelicula(request):
    formulario_pelicula = FormularioPelicula(request.POST, request.FILES)
    if request.method == 'POST':
        if formulario_pelicula.is_valid():
            datos = formulario_pelicula.cleaned_data
            pelicula = Pelicula()
            pelicula.nombre_pelicula = datos.get('nombre_pelicula')
            pelicula.genero = datos.get('genero')
            pelicula.sinopsis = datos.get('sinopsis')
            pelicula.clasificacion = datos.get('clasificacion')
            pelicula.fechaLanzamiento = datos.get('fechaLanzamiento')
            pelicula.duracion = datos.get('duracion')
            pelicula.proyeccion = datos.get('proyeccion')
            pelicula.director = datos.get('director')
            pelicula.protagonistas = datos.get('protagonistas')
            pelicula.imagen = datos.get('imagen')
            pelicula.save()
            messages.success(request, 'Pelicula registrada correctamente')
            return redirect(verPelicula)
        else:
            messages.error(request, 'Esta pelicula ya esta registrada')
                 
   
    
    context = {
        'f': formulario_pelicula 
    }

    return render(request,'pelicula/registrar_pelicula.html', context)

def editarPelicula(request):
    nombre = request.GET['nombre_pelicula']
    pelicula = Pelicula.objects.get(nombre_pelicula = nombre)
    if request.method == 'POST':
        formulario_editar = FormularioEditarPelicula(request.POST)
        if formulario_editar.is_valid():
            datos = formulario_editar.cleaned_data
            pelicula.proyeccion = datos.get('proyeccion')
            pelicula.save()
            messages.success(request, 'Datos de la pelicula actualizados correctamente')
            return redirect(verPelicula)
    else:
        formulario_editar = FormularioEditarPelicula(instance = pelicula)
    context = {
        'f': formulario_editar 
    }

    return render(request,'pelicula/editar_pelicula.html', context)

def verPelicula(request):
    lista = Pelicula.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'pelicula/ver_pelicula.html', context)

def verSala(request):
    lista = Sala.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'salas/ver_salas.html', context)





    


