from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioPersona
from apps.modelo.models import Persona, Rol
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json, crypt

def registrarse(request):
    listaR = Rol.objects.all()
    formulario_persona = FormularioPersona(request.POST)
    if request.method == 'POST':
        if formulario_persona.is_valid():
            datos = formulario_persona.cleaned_data
            persona = Persona ()
            persona.is_superuser = True
            persona.is_staff = False
            persona.username = datos.get("username")
            persona.set_password(datos.get("password"))
            persona.first_name = datos.get("first_name")
            persona.last_name = datos.get("last_name")
            persona.fechaNacimiento = datos.get('fechaNacimiento')
            persona.edad = datos.get('edad')
            persona.rol = datos.get('rol')
            persona.email = datos.get('email')
            persona.save()
            messages.success(request, 'Te registraste correctamentee')
            return redirect('/cine')
        else:
            messages.error(request, 'Cedula ya registrada')
                 
   
    
    context = {
        'f': formulario_persona,
        'listaR':listaR, 
    }
    
    return render(request,'persona/registrar_persona.html', context)

def ingresar(request):
    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['emailForm']
            clave = request.POST['claveForm']
            user = authenticate(username = usuario, password = clave)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('cartelera'))
                else:
                    print ('Usuario desactivado')
            else:
                print('Usuario y/o contrasenia invalida')
            
    else:
        formulario = FormularioLogin()

    context = {
        'formulario': formulario
            }
    
    return render (request, 'persona/registrar_persona.html', context)                
	
				
	
		

	
	
    
    



