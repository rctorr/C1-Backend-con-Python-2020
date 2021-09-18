`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 01`](../Readme.md) > Ejemplo-01
## Entornos virtuales e instalación de Django

### OBJETIVO
- Conocer los entornos virtuales y su aplicación
- Conocer el framework Django y su instalación
- Conocer como distribuir entornos virtuales al equipo de desarrollo

#### REQUISITOS
1. Descargar el repositorio
1. Usar la carpeta de trabajo `Sesion-01/Ejemplo-01`

#### DESARROLLO

1. Crear un entorno virtual llamado `django` para el proyecto usando el siguiente comando:

```sh
conda create -n django python=3
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/rctorr/miniconda3/envs/django

  added / updated specs:
    - python=3


The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-4.5-1_gnu
  ca-certificates    pkgs/main/linux-64::ca-certificates-2021.7.5-h06a4308_1
  certifi            pkgs/main/linux-64::certifi-2021.5.30-py39h06a4308_0
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.35.1-h7274673_9
  libffi             pkgs/main/linux-64::libffi-3.3-he6710b0_2
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-9.3.0-h5101ec6_17
  libgomp            pkgs/main/linux-64::libgomp-9.3.0-h5101ec6_17
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-9.3.0-hd4cf53a_17
  ncurses            pkgs/main/linux-64::ncurses-6.2-he6710b0_1
  openssl            pkgs/main/linux-64::openssl-1.1.1l-h7f8727e_0
  pip                pkgs/main/linux-64::pip-21.2.4-py37h06a4308_0
  python             pkgs/main/linux-64::python-3.9.7-h12debd9_1
  readline           pkgs/main/linux-64::readline-8.1-h27cfd23_0
  setuptools         pkgs/main/linux-64::setuptools-58.0.4-py39h06a4308_0
  sqlite             pkgs/main/linux-64::sqlite-3.36.0-hc218d9a_0
  tk                 pkgs/main/linux-64::tk-8.6.10-hbc83047_0
  tzdata             pkgs/main/noarch::tzdata-2021a-h5d7bf9c_0
  wheel              pkgs/main/noarch::wheel-0.37.0-pyhd3eb1b0_1
  xz                 pkgs/main/linux-64::xz-5.2.5-h7b6447c_0
  zlib               pkgs/main/linux-64::zlib-1.2.11-h7b6447c_3


Proceed ([y]/n)? 

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate django
#
# To deactivate an active environment, use
#
#     $ conda deactivate
   
```

__Nota:__ Revisar concepto de **entorno virtual**

__Activaremos el entorno virtual:__

```sh
(base) $ conda activate django
(django) $ 
```
   
__Para desactivar el nuevo entorno se realiza con:__

```sh
(django) $ conda deactivate
(base) $
```

__Activaremos nuevamente el entorno para continuar:__

```sh
(base) $ conda activate django
(django) $ 
```
***

2. PInstalación del paquete / framework Django:

__La instalación se realiza con el comando pip dentro del entorno virtual:__

```sh
(django) $ pip install django
Collecting django
  Using cached Django-3.2.7-py3-none-any.whl (7.9 MB)
Collecting pytz
  Using cached pytz-2021.1-py2.py3-none-any.whl (510 kB)
Collecting asgiref<4,>=3.3.2
  Using cached asgiref-3.4.1-py3-none-any.whl (25 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Installing collected packages: sqlparse, pytz, asgiref, django
Successfully installed asgiref-3.4.1 django-3.2.7 pytz-2021.1 sqlparse-0.4.2
```

__La página principal del framework Django:__
- Sitio principal [https://www.djangoproject.com](https://docs.djangoproject.com/en/3.1/)
- Documentación oficial: [https://docs.djangoproject.com/en/3.1/](https://docs.djangoproject.com/en/3.1/)
***

3. Respaldando y restaurando un entorno virtual

__Para respaldar un entorno virtual se realiza con:__

```sh
(django) $ pip freeze > requeriments.txt
(django) $ cat requeriments.txt
asgiref==3.4.1
certifi==2021.5.30
Django==3.2.7
pytz==2021.1
sqlparse==0.4.2
```
   
__Para restaurar un entorno virtual se realiza con:__

```sh
(django) $ pip3 install -r requeriments.txt 
Requirement already satisfied: asgiref==3.4.1 in /home/rctorr/miniconda3/envs/django/lib/python3.9/site-packages (from -r requeriments.txt (line 1)) (3.4.1)
Requirement already satisfied: certifi==2021.5.30 in /home/rctorr/miniconda3/envs/django/lib/python3.9/site-packages (from -r requeriments.txt (line 2)) (2021.5.30)
Requirement already satisfied: Django==3.2.7 in /home/rctorr/miniconda3/envs/django/lib/python3.9/site-packages (from -r requeriments.txt (line 3)) (3.2.7)
Requirement already satisfied: pytz==2021.1 in /home/rctorr/miniconda3/envs/django/lib/python3.9/site-packages (from -r requeriments.txt (line 4)) (2021.1)
Requirement already satisfied: sqlparse==0.4.2 in /home/rctorr/miniconda3/envs/django/lib/python3.9/site-packages (from -r requeriments.txt (line 5)) (0.4.2)
```

__Mostramos la lista de módulos instalados:__

```sh
(django) $ pip3 freeze
asgiref==3.4.1
certifi==2021.5.30
Django==3.2.7
pytz==2021.1
sqlparse==0.4.2
```
   
Ahora estamos listos para continuar con Django.
***
