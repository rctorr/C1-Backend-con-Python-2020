from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Tour, Zona

from .serializers import ZonaSerializer, TourSerializer
from rest_framework import viewsets

# Bedutravels/tours/views.py

# Create your views here.
@login_required()
def index(request):
	""" Atiende la petición GET / """
	tours = Tour.objects.filter(zonaSalida__nombre = "CDMX")

	return render(request, "tours/index.html", {"tours":tours})

# Vistas basadas en clases para Django Rest
class ZonaViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla Zona
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre todos las Zonas disponibles.
   queryset = Zona.objects.all().order_by('id')
   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = ZonaSerializer


class TourViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla Tour
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre todos los tours disponibles.
   queryset = Tour.objects.all().order_by('id')
   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = TourSerializer

