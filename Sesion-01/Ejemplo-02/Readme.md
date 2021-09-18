
[`Backend con Python`](../../Readme.md) > [`Sesión 01`](../Readme.md) > Ejemplo-02
## Iniciar la construcción de una aplicación web con Django

### OBJETIVOS
- Conocer como iniciar un proyecto en Django
- Conocer como crear una aplicación
- Conocer y definir una ruta en Django
- Conocer y definir una vista asociada a la ruta

#### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-01/Ejemplo-02`
1. Activar el entorno virtual __django__

#### DESARROLLO
1. Crear el proyecto __Banco__ con Django y cambiándonos a la carpeta del proyecto:

```sh
(django) $ django-admin startproject Banco
(django) $
```

2. Ingresamos al directorio creado y lo visualizamos

```sh
(django) $ cd Banco
(django) $ tree
.
├── Banco
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

1 directory, 6 files
```

3. Crear la aplicación __tarjeta__ con el comando:

```sh
(django) $ python3 manage.py startapp tarjeta
(django) $ tree
.
├── Banco
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   └── settings.cpython-39.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── tarjeta
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

4 directories, 15 files
```
***

4. Ejecutar el proyecto __Banco__ con:

```sh
(django) $ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 18, 2021 - 06:57:11
Django version 3.2.7, using settings 'Banco.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
   
Si se abre la url indicada (http://127.0.0.1:8000/), se observará lo mismo que el "hola mundo!".

![hola django](img/hola-django.png)

así que sigamos un poco más adelante, nuestro objetivo es mostrar la página `index.html` pero como parte de la aplicación web.
   
__Nota:__ Como el servidor bloquea la terminal, vamos a dejar esta terminal aquí y para los siguiente comandos abrir otra terminal, activar el entorno virtual django.
   
```sh
(base) $ conda activate django
(django) $
```

5. Agrega la aplicación __tarjeta__ a la configuración en el archivo `Banco/Banco/settings.py`:

```python
# Application definition

INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'tarjeta',
]   
```
   
__Flujo de una petición y su respuesta a traves de los componentes de Django__

![Flujo de django](img/django-circle-flow.jpg)

6. Agrega información regional a la configuración en el archivo `Banco/Banco/settings.py`:

```python
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'
```
   
Esto permite que el administrador de django esté en español, además de que el tratamiento de horas y fechas serán referidas a la zona horaria de la Ciudad de México.

7. Redirigir la url `/` con las rutas generales del proyecto __Banco__ hacia las rutas de la aplicación __tarjeta__ que será nuestra aplicación principal en este caso.

```
url / -> Banco/Banco/urls.py -> Banco/tarjeta/urls.py
```

__En el archivo `Banco/Banco/urls.py` agregar lo siguiente:__

```python
from django.contrib import admin
from django.urls import path, include  # modificada

urlpatterns = [
   path('', include("tours.urls")),  # agregada
   path('admin/', admin.site.urls),
]
```
   
En la vetana donde se está ejecutando el proyecto __Banco__ se puede observar el siguiente mensaje de error:

```sh
...
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 972, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 984, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tarjeta.urls'
```

Lo que indica que nos falta crear el archivo `urls.py` dentro de la carpeta `Banco/tarjeta/`

8. Asociar la url `/` con las rutas de la aplicación __tarjeta__ a una vista:

```
url / -> Banco/tarjeta/urls.py -> Banco/tarjeta/views.py
```

__Crear el archivo `Banco/tarjeta/urls.py` con el siguiente contenido:__
   
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
```
   
__Reiniciar Django para observar el resultado:__

```sh
...
File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 972, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/rctorr/Escritorio/TECP0006FSPYOL2102-BaPy/Sesion-01/Ejemplo-02/Banco/tarjeta/urls.py", line 5, in <module>
    path('', views.index, name="index"),
AttributeError: module 'tarjeta.views' has no attribute 'index'
```

Lo que indica que en el archivo `tarjeta/views.py` no existe una función llamada `index`, así que toca agregar dicha función.

9. Agregar la función/vista `index()` al archivo `tarjeta/views.py` con el siguiente contenido:

```python
from django.http import HttpResponse

# Create your views here.
def index(request):
   """ Vista para atender la petición de la url / """
   return HttpResponse("<h2>Soy la página de inicio! Hecho con Django!</h2>")
```

__Nota: Si la aplicación Django muestra el link para abrir la aplicación, entonces reiniciar Django__

__El resultado debería ser el siguiente:__

![Banco Inicio](img/banco-inicio.png)
***
