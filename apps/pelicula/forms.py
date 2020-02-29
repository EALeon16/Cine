from django import forms 
from apps.modelo.models import Pelicula, Persona, Sala
class FormularioPelicula(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ["nombre_pelicula", "genero","sinopsis", "clasificacion", "proyeccion","fechaLanzamiento","duracion","director","protagonistas","imagen"]

class FormularioEditarPelicula(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ["proyeccion"]





        





