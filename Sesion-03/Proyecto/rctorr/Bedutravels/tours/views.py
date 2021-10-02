from django.shortcuts import render, redirect
from .models import Tour

# Bedutravels/tours/views.py

# Create your views here.
def index(request):
	""" Atiende la petición GET / """
	tours = Tour.objects.filter(zonaSalida__nombre = "CDMX")

	return render(request, "tours/index.html", {"tours":tours})

def login(request):
    """ Atiende las peticiones de GET y POST /login/ """
    usuario_valido = ("rctorr", "rctorr")

    if request.method == "POST":
        # Se obtienen los datos del formulario
        user = request.POST["username"]
        passwd = request.POST["password"]
        usuario_form = (user, passwd)
        if usuario_form == usuario_valido:
            # Tenemos usuario válido, redireccionamos a index
            return redirect("/")
        else:
            # Usuario malo
            msg = "Datos incorrectos, intente de nuevo!"
    else:
        # Si no hay datos POST entonces es GET y enviamos formulario
        msg = ""

    return render(request, "registration/login.html",
        {
            "msg":msg,
        }
    )
