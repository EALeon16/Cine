from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Pelicula(models.Model):
	listaGenero =(
		('A', '"A" - Aptas para todo publico'),
		('B', '"B" - Películas para adolescentes de 12 años en adelante'),
        ('B15', '"B15" - Película no recomendable para menores de 15 años de edad'),
		('C', '"C" - Películas para adultos de 18 años en adelante'),
        ('D', '"D" - Películas para adultos, con sexo explícito'),
		
	)
	listaProyeccion =(
		('si', 'Si'),
		('no', 'No'),
       
		
	)
	pelicula_id = models.AutoField(primary_key = True)
	nombre_pelicula = models.CharField(max_length=75, unique = True, null=False)
	genero = models.CharField(max_length=50, null=False)
	sinopsis = models.CharField(max_length=50, null=False)
	clasificacion = models.CharField(max_length=15, choices = listaGenero, default= '"A" - Aptas para todo publico', null=False)
	fechaLanzamiento =  models.DateField(auto_now = False, auto_now_add = False, null = False)
	duracion = models.CharField(max_length=25)
	proyeccion = models.CharField(max_length=15,null=False, choices = listaProyeccion)
	director = models.CharField(max_length=25)
	protagonistas = models.TextField(max_length=50, default='n/a')
	imagen = models.ImageField(upload_to="portadas", null=True)

class Rol(models.Model):
	rol_id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=20, null= False)	
	

class Persona(AbstractUser):
	persona_id = models.AutoField(primary_key = True)
	fechaNacimiento =  models.DateField(auto_now = False, auto_now_add = False, null = True)
	edad = models.CharField(max_length=25, null = True)
	rol = models.ForeignKey(
		'Rol', 
		on_delete = models.CASCADE,
		null = True,
	)
	def __str__(self):
		return '{}{}'.format(self.first_name, self.last_name)

class Sala(models.Model):
	sala_id = models.AutoField(primary_key = True)
	nombre_sala = models.CharField(max_length=75, unique = True, null=False)
	nro_asientos = models.IntegerField(max_length=50, null=False)

class Horario(models.Model):
	listaCalidad =(
		('2D', '2D'),
		('2D-4K', '2D-4K'),
		('3D', '3D'),
		('3D-4K', '3D-4K'),
       
		
	)
	horario_id = models.AutoField(primary_key = True)
	hora_pelicula = models.TimeField(null=False)
	fecha_pelicua = models.DateField(auto_now = False, auto_now_add = False, null = False)
	calidad_pelicula = models.CharField(max_length=50, null=False,choices = listaCalidad, default='2D')
	pelicula = models.ForeignKey(
		'Pelicula', 
		on_delete = models.CASCADE,
	)
	sala = models.ForeignKey(
		'Sala', 
		on_delete = models.CASCADE,
	)
	
class Boleto(models.Model):
	boleto_id = models.AutoField(primary_key = True)
	cantidad_boletoN = models.IntegerField(max_length=10, null=False)
	cantidad_boletoE = models.IntegerField(max_length=10, null=False)
	total_boleto = models.IntegerField(max_length=10, null=False)
	precio_total = models.DecimalField(max_digits=10, decimal_places=3, null=False)
	persona = models.ForeignKey(
		'Persona', 
		on_delete = models.CASCADE,
	)
	horario = models.ForeignKey(
		'Horario', 
		on_delete = models.CASCADE,
	)
	


   

