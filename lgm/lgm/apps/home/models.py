from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_profile(models.Model):
	
	def url(self, filename):
		ruta = "MultimediaData/User/%s/%s"%(self.user.username,filename)
		return ruta

	user 		=	models.OneToOneField(User)
	photo 		=	models.ImageField(upload_to=url)
	telefono 	=	models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username


class Clase(models.Model):
	nombre = models.CharField(max_length = 100)
	codigo = models.CharField(max_length = 100)

	def __unicode__ (self):
		return self.nombre

class Enfermedad(models.Model):
	nombre = models.CharField(max_length = 100)
	origen = models.TextField(max_length = 500)
	curso  = models.CharField(max_length = 100)
	frecuencia = models.CharField(max_length =100)
	clase = models.ForeignKey(Clase)

	def __unicode__ (self):
		return self.nombre

	

class Ejercicio(models.Model):
	nombre = models.CharField(max_length = 100)
	tiempo = models.DateTimeField(auto_now_add = True)
	series = models.CharField(max_length = 100)

	def __unicode__ (self):
		return self.nombre	


class Rutina(models.Model):
	nombre        = models.CharField(max_length = 100)
	clasificacion = models.CharField(max_length = 100)
	fechahora     =  models.DateTimeField(auto_now_add = True)
	ejercicio      = models.ManyToManyField(Ejercicio, null = True, blank= True)

	def __unicode__ (self):
		return self.nombre


class Producto(models.Model):
	def url(self, filename):
		ruta = "MultimediaData/Productos/%s/%s"%(self.nombre, str(filename))
		return rutams

	nombre      = models.CharField(max_length = 100)
	precio      = models.CharField(max_length = 100)
	descripcion = models.TextField(max_length=100)
	stock       = models.IntegerField()
	imagen     = models.ImageField(upload_to = url, null = True, blank = True)

	def __unicode__ (self):
		return self.nombre



class Dieta(models.Model):
	clasificacion= models.CharField(max_length = 100)
	horario      = models.CharField(max_length = 100)
	suplementos  = models.TextField(max_length=100)
	porciones    = models.CharField(max_length=100)
	producto     = models.ManyToManyField(Producto, null= True, blank = True)

 	def __unicode__ (self):
		return self.clasificacion


class Valoracion(models.Model):
	masamuscular  = models.CharField(max_length = 100)
	fechahora     = models.DateTimeField(max_length = 100)
	peso          = models.CharField(max_length=100)
	grasaviceral  = models.CharField(max_length=100)
	grasacorporal = models.CharField(max_length=100)
	pagua         = models.CharField(max_length=100)
	masaosea      = models.CharField(max_length=100)
	edadmetabolica= models.CharField(max_length=100)
	bmr           = models.CharField(max_length=100)

	def __unicode__ (self):
		return self.masamuscular


class Persona (models.Model):
	nombre          = models.CharField(max_length = 100)
	apellidos       = models.CharField(max_length = 100)
	genero          = models.TextField(max_length=100)
	documento       = models.CharField(max_length=100)
	fechanacimiento = models.CharField(max_length=100)
	enfermedad      = models.ManyToManyField(Enfermedad, null= True, blank =True)
	user            = models.ForeignKey(User)

	def __unicode__ (self):
		return self.nombre


