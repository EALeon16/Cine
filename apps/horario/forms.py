from django import forms 
from apps.modelo.models import Horario
class FormularioHorario(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ["hora_pelicula", "fecha_pelicua", "sala", "calidad_pelicula"]

