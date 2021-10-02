from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Tour

# Bedutravels/tours/views.py

# Create your views here.
@login_required()
def index(request):
	""" Atiende la petición GET / """
	tours = Tour.objects.filter(zonaSalida__nombre = "CDMX")

	return render(request, "tours/index.html", {"tours":tours})

