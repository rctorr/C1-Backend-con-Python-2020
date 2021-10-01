from django.db import models

# Create your models here.
class User(models.Model):
	""" Define la tabla User """
	nombre = models.CharField(max_length=45)
	apellidos = models.CharField(max_length=45, null=True, blank=True)
	email = models.EmailField()
	fecha_nacimiento = models.DateField(null=True, blank=True)
	clave = models.CharField(max_length=45, null=True, blank=True)
	tipo = models.CharField(max_length=45, null=True, blank=True)
	# genero -> ("H", "M")
	GENERO = [
		("H", "Hombre"),
		("M", "Mujer"),
		("O", "Otro"),
		("N", "Ninguno"),
	]
	genero = models.CharField(max_length=1, choices=GENERO)
