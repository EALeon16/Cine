from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioSala
from django.http import HttpResponse
from django.views.generic import View
import datetime
from django.template.loader import get_template
from apps.pdf.utileria import render_pdf

from apps.modelo.models import Sala, Persona, Horario, Boleto, Pelicula



def pdfBoleto(request):
    bol = request.GET.get('nro')
    now = datetime.date.today()
    template = get_template('boleto/pdf.html')
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
    html = template.render(context)
    
    
    pdf = render_pdf('boleto/pdf.html', context)
    return HttpResponse(pdf, content_type="application/pdf")    



   
