from django import forms 
from apps.modelo.models import Sala

class FormularioSala(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ["nombre_sala", "nro_asientos"]