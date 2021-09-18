`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 01`](../Readme.md) > Ejemplo-03
## Agregar la página de inicio ya maquetada a la aplicación web

### OBJETIVOS
- Conocer como agregar páginas ya maquetadas por medio de las plantillas con Django.
- Conocer como configurar y agregar los archivos estáticos en una aplicación web con Django.
- Contar con la página de inicio del proyecto Bedutravels disponible con Django.

#### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-01/Ejemplo-03/django/`
1. Activar el entorno virtual __django__
1. Página de inicio maquetada del proyecto __Banco__

   ![](img/banco-inicio.png)

#### DESARROLLO
1. Ejecutar el proyecto __Banco__ con:

```sh
(django) $ python3 manage.py runserver   
```
***

1. Haciendo uso de las plantillas de Django integrar la página de inicio maquetada que se encuentra en `public_html/index.html`.

__Crear las carpetas `Banco/tarjeta/templates/tarjeta` para almacenar las plantillas o documentos html para la aplicación `tarjeta`:__

```sh
(base) $ mkdir -p tarjeta/templates/tarjeta
```

__Copiar el archivo `public_html/index.html` dentro de la carpeta `Banco/tarjeta/templates/tarjeta/`:__

```sh
(base) $ cp public_html/index.html Banco/tarjeta/templates/tarjeta
```

__Modificar la función `index()` en el archivo `tarjeta/views.py` para hacer uso de las plantillas (templates)__

```python
from django.shortcuts import render

# Create your views here.
def index(request):
   """ Vista para atender la petición de la url / """
   return render(request, "tarjeta/index.html")
```

Por omisión, Django busca los archivos html en la carpeta `proyecto/aplicacion/templates/aplicacion/`

__El resultado en el navegador debería de ser el siguiente:__

![Plantilla Inicio](img/plantilla-inicio.png)

Hasta aquí ya podemos ver el html, pero ¿y los estilos y las imágenes?

Como son archivos estáticos aún no hemos autorizado a que se puedan ver, así que continuemos.
***

1. Agregando acceso a los archivos estáticos (ruta y vista)

__Crear la carpeta `Banco/tarjeta/static/tarjeta/`:__

```sh
(base) $ mkdir -p tarjeta/static/tarjeta
```

__Copiar las carpetas de los archivos estáticos (css, fonts, images y js):__

```sh
(base) $ cp -av public_html/css public_html/fonts public_html/images public_html/js Banco/tarjeta/static/tarjeta/

(base) $ tree tarjeta/static/
tarjeta/static/
└── tarjeta
    ├── css
    ├── fonts
    ├── images
    └── js

5 directories, 0 files
```

__Finalmente hay que modificar la ruta en el archivo `index.html` para que usen el sistema de Django__

Todas las url relativas o absolutas ahora tienen que ser absolutas e iniciar con `/static/tarjeta/`, un ejemplos se muestra a continuación:

```html
<!-- Animate.css -->
<link rel="stylesheet" href="/static/tarjeta/css/index.css">
```
Remplazar todas las coincidencias.

__Actualizar el navegador y entonces se debería de ver la página mostrada al inicio__

**Nota:** Si no funciona realizar lo siguiente:
- Recargar la página forzado actualizar el cache del navegador con `Control+Shift+R`.
- En la ventana donde se está ejecutando el proyecto, deterlo y volver a iniciarlo.
- Usar una ventana de incógnito.
- Pedir ayuda a un experto (que no lo vas a encontrar en clase!)

Si si funciona entonces:
- Misión cumplida!
