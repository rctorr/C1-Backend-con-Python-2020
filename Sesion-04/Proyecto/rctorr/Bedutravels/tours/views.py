from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Tour

# Bedutravels/tours/views.py

@login_required
def index(request):
    """ Atiende la petición GET / """
    tours = Tour.objects.filter(zonaSalida__nombre = "CDMX")
    es_editor = request.user.groups.filter(name="editores").exists()

    return render(
                  request,
                  "tours/index.html",
                  {
                    "tours":tours,
                    "es_editor": es_editor,
                  }
                )

@login_required()
def eliminar_tour(request, idTour):
    """
    Atiende la petición GET
       /tour/eliminar/<int:idTour>/
    """
    # Se obtienen los objetos correspondientes a los id's
    tour = Tour.objects.get(pk=idTour)

    # Se elimina el tour
    tour.delete()

    return redirect("/")
