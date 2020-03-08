from django import forms 
from apps.modelo.models import Boleto
class FormularioBoleto(forms.ModelForm):
    class Meta:
        model = Boleto
        fields = ["cantidad_boletoN", "cantidad_boletoE", "precio_total", "total_boleto"]
        labels = {
			'cantidad_boletoN':'cntBolN',
			'cantidad_boletoE':'cntBolE',
			'precio_total':'Precio Total',
			'total_boleto':'Cantidad de Boletos',
		}


     