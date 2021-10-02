from django.contrib.auth import authenticate, login
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

def login_user(request):
    """ Atiende las peticiones de GET y POST /login/ """

    if request.method == "POST":
        # Se obtienen los datos del formulario
        user = request.POST["username"]
        passwd = request.POST["password"]
        next_ = request.GET.get("next", "/")
        user_obj = authenticate(username=user, password=passwd)
        if user_obj != None:
            # Tenemos usuario válido, redireccionamos a index
            login(request, user_obj)  # crea la sesión usando cookies
            return redirect(next_)
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
