from django.contrib import admin
from .models import User, Zona, Tour

# Personalizando modelos en el admin
class UserAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "apellidos", "email", "fecha_nacimiento",
        "genero", "tipo")

class ZonaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "descripcion", "latitud", "longitud")

class TourAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "descripcion", "operador", "zonaSalida", "zonaLlegada")

admin.site.register(User, UserAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(Tour, TourAdmin)
