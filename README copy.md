# Actividad3

## Configuración del Entorno
### Instalación de módulos Virtualenv (Sistemas basados en Unix)
```
$ virtualenv env
$ source env/bin/activate
```
### Instalación de módulos Virtualenv (Sistemas basados en Windows)
```
# python -m venv env
# .\env\Scripts\activate
```
### Instalación de módulos - Almacenamiento SQLite
```
### Puedes usar cualquiera de estos comandos
$ .\env\Scripts\pip3 install -r requirements.txt
or
$ pip3 install -r requirements.txt

```
## Inicio de la Aplicación
### Creación de tablas
### Si ya se encuentra creado esto no lo concideres
```
$ python manage.py makemigrations
$ python manage.py migrate
```
### Creación de superusuario de la app
### Si ya se encuentra creado esto no lo concideres
```
$ python manage.py createsuperuser
```
### Inicio de la aplicación (modo desarrollo)
```
$ python manage.py runserver # Puerto por defecto 8000
```
### Inicio de la app - Puerto personalizado
```
# python manage.py runserver 0.0.0.0:<your_port>
```
### Acceso a la app web en el navegador:
```
http://127.0.0.1:8000/
```