from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  FormularioBoleto
from apps.modelo.models import Pelicula, Persona, Sala, Horario, Boleto
from django.db.models import Sum

def vistaBoleto(request):
    horario = request.GET.get('id')
    idp = request.user.persona_id
    idpersona = Persona.objects.get(persona_id = idp)
    horarios = Horario.objects.get(horario_id = horario)
    total_paid = list(Boleto.objects.filter(horario_id = horario).aggregate(Sum('total_boleto')).values())[0]
    if(total_paid == None):
        total_paid = 0
    disponibles = 30 - total_paid
    formulario_boleto = FormularioBoleto(request.POST)
    if request.method == 'POST':
        if total_paid <= 30:
            if formulario_boleto.is_valid():
                boleto = Boleto()
                datos = formulario_boleto.cleaned_data
                if disponibles + datos.get('total_boleto') < 30:
                    boleto.precio_total = datos.get('precio_total')
                    boleto.cantidad_boletoN = datos.get('cantidad_boletoN')

                    boleto.total_boleto = datos.get('total_boleto')
                    boleto.cantidad_boletoE = datos.get('cantidad_boletoE')
                    
                    boleto.persona = idpersona
                    boleto.horario = horarios
                    boleto.save()
                    messages.success(request, 'Compra realizada correctamente')
                    return redirect('/historailCompras') 
                else:
                    messages.error(request, 'Cantidad de Boletos excede a los disponibles')
        else:
            return render(request,'boleto/no_boletos.html')        
                 
   
    
    context = {
        'f': formulario_boleto,
        'horario':horario,
        'total_paid':total_paid,
        'disponibles': disponibles
    }
    return render(request,'boleto/adquirir_boleto.html',context)


