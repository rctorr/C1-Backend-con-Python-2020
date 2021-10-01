from django.shortcuts import render
from .models import Tour

# Bedutravels/tours/views.py

# Create your views here.
def index(request):
	""" Atiende la petición GET / """
	tours = Tour.objects.filter(zonaSalida__nombre = "CDMX")

	return render(request, "tours/index.html", {"tours":tours})

