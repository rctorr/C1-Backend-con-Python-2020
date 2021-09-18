from django.shortcuts import render

# Create your views here.
def index(request):
   """ Vista para atender la petición de la url / """
   return render(request, "tarjeta/index.html")
