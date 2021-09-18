from django.http import HttpResponse

# Banco/tarjeta/views.py

# Create your views here.
def index(request):
   """ Vista para atender la petición GET / """
   return HttpResponse("<h2>Soy la página de inicio! Hecho con Django! (Hecho por @rctorr)</h2>")
