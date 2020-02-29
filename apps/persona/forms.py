from django import forms 
from apps.modelo.models import Persona
class FormularioPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [ "fechaNacimiento", "edad", "rol","first_name", "last_name","email", "username", "password"]
class FormularioLogin(forms.Form):   
    fields = [ "emailForm", "claveForm"]     