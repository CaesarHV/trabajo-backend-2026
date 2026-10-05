# Proyecto Django - API REST Biblioteca

## Descripción

Este proyecto corresponde al desarrollo de una API REST utilizando Django y Django REST Framework.

El proyecto permite gestionar información de países mediante una API REST, utilizando operaciones CRUD y persistencia de datos en una base de datos MySQL.

La aplicación utiliza variables de entorno mediante un archivo `.env` para mantener separada la configuración sensible del proyecto.

---

## Requisitos

Para ejecutar este proyecto se necesita tener instalado:

* Python 3.x
* Django
* Django REST Framework
* MySQL
* MySQL Connector/Python o `mysqlclient`
* `pip`

Se recomienda utilizar un entorno virtual de Python.

---

## Entorno virtual

Para crear un entorno virtual se utiliza:

```bash
python -m venv venv
```

Para activar el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Una vez activado, la terminal mostrará el nombre del entorno virtual.

Para actualizar `pip`:

```bash
python -m pip install --upgrade pip
```

---

## Instalación de Django

Para instalar Django:

```bash
pip install django
```

También se instala Django REST Framework:

```bash
pip install djangorestframework
```

Para utilizar variables de entorno:

```bash
pip install python-decouple
```

Para trabajar con MySQL:

```bash
pip install mysqlclient
```

---

## Creación del proyecto

El proyecto Django se denomina:

```text
motor_django
```

La aplicación principal se denomina:

```text
app_encuestas
```

El proyecto fue creado utilizando Django y posteriormente se agregó la aplicación correspondiente.

La estructura principal es:

```text
motor_django/
│
├── manage.py
├── .env
├── database.sql
├── requirements.txt
├── README.md
│
├── motor_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── app_encuestas/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── tests.py
    ├── migrations/
    └── fixtures/
```

---

## Configuración de Django

En el archivo `settings.py` se encuentra configurada la aplicación:

```python
'app_encuestas',
```

También se encuentra instalado Django REST Framework:

```python
'rest_framework',
```

La configuración de seguridad utiliza variables de entorno para obtener la clave secreta:

```python
SECRET_KEY = config('SECRET_KEY')
```

La aplicación se ejecuta con:

```python
DEBUG = False
```

Y se permiten las conexiones locales:

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

---

## Base de datos MySQL

El proyecto utiliza MySQL como sistema gestor de base de datos.

La base de datos utilizada se denomina:

```text
pais
```

La configuración de conexión se obtiene desde el archivo `.env`.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```

---

## Creación de la base de datos

El proyecto incluye el archivo:

```text
database.sql
```

Este archivo contiene las instrucciones SQL necesarias para crear la base de datos, crear el usuario y asignar sus permisos.

Ejemplo:

```sql
CREATE DATABASE IF NOT EXISTS pais;

CREATE USER 'cesar'@'%' IDENTIFIED BY '123';

GRANT ALL PRIVILEGES ON pais.* TO 'cesar'@'%';

FLUSH PRIVILEGES;
```

El archivo `database.sql` debe ejecutarse en MySQL antes de realizar las migraciones del proyecto.

---

## Migraciones

Las migraciones permiten crear y actualizar las tablas de la base de datos de acuerdo con los modelos definidos en Django.

Para generar migraciones:

```bash
python manage.py makemigrations
```

Para aplicarlas:

```bash
python manage.py migrate
```

Las migraciones generadas se encuentran dentro de:

```text
app_encuestas/migrations/
```

---

## Variables de entorno

El proyecto utiliza `python-decouple` para administrar las variables de configuración.

El archivo `.env` se encuentra en la raíz del proyecto, al mismo nivel que `manage.py`.

Las variables utilizadas son:

```env
DB_NAME=pais
DB_USER=cesar
DB_PASSWORD=123
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY='cadena_de_caracteres_django_secret_key'
```

Estas variables son utilizadas desde `settings.py` mediante:

```python
from decouple import config
```

De esta forma, las credenciales de conexión y la clave secreta no se escriben directamente en `settings.py`.

---

## Django REST Framework

El proyecto utiliza Django REST Framework para implementar la API REST.

La aplicación se encuentra agregada en `INSTALLED_APPS`:

```python
'rest_framework',
```

Django REST Framework permite crear los endpoints de la API y realizar las operaciones correspondientes sobre los modelos.

---

## Modelos

Los modelos del proyecto se encuentran definidos en:

```text
app_encuestas/models.py
```

El proyecto contiene diferentes entidades relacionadas con la gestión de una biblioteca.

Entre ellas se encuentran:

* País
* Región
* Provincia
* Comuna
* Dirección
* Biblioteca
* Autor
* Género
* Subgénero
* Editorial
* Idioma
* Edición
* Libro
* Estado
* Ubicación
* Inventario
* Usuario
* Préstamo

Estos modelos permiten representar la información y las relaciones correspondientes a la estructura de datos del proyecto.

---

## Serializers

Los serializers se encuentran en:

```text
app_encuestas/serializer.py
```

Actualmente se utiliza `PaisSerializer` para transformar los objetos del modelo `Pais` a un formato JSON y validar los datos recibidos mediante la API.

```python
from rest_framework import serializers
from .models import Pais

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'
```

---

## ViewSets

Las vistas de la API se encuentran en:

```text
app_encuestas/views.py
```

Se utiliza `ModelViewSet` para implementar las operaciones CRUD.

```python
class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
```

`ModelViewSet` permite trabajar con las operaciones:

* GET
* POST
* PUT
* PATCH
* DELETE

---

## URLs y Router

Las rutas de la API se configuran en:

```text
motor_django/urls.py
```

Se utiliza `DefaultRouter` de Django REST Framework:

```python
router = DefaultRouter()
router.register(r'paises', views.PaisViewSet)
```

Las rutas de la API se incluyen mediante:

```python
path('api/', include(router.urls)),
```

Por lo tanto, el endpoint principal es:

```text
http://127.0.0.1:8000/api/paises/
```

---

## Ejecución del proyecto

Para ejecutar el proyecto se debe activar primero el entorno virtual:

```bash
venv\Scripts\activate
```

Luego se instalan las dependencias:

```bash
pip install -r requirements.txt
```

Se comprueba que el proyecto no tenga errores:

```bash
python manage.py check
```

Se aplican las migraciones:

```bash
python manage.py migrate
```

Finalmente se inicia el servidor:

```bash
python manage.py runserver
```

El proyecto estará disponible en:

```text
http://127.0.0.1:8000/
```

---

## API REST

El endpoint implementado para la gestión de países es:

```text
http://127.0.0.1:8000/api/paises/
```

### GET - Listar países

Permite obtener todos los países registrados:

```http
GET /api/paises/
```

### GET - Obtener un país por ID

Permite obtener un país específico:

```http
GET /api/paises/2/
```

### POST - Crear un país

Permite registrar un nuevo país:

```http
POST /api/paises/
```

Ejemplo de información enviada:

```json
{
    "nombre": "Chile",
    "nacionalidad": "Chilena",
    "iso_2": "CL",
    "iso_3": "CHL",
    "habilitado": true
}
```

### PUT - Actualizar un país

Permite reemplazar completamente la información de un país:

```http
PUT /api/paises/2/
```

Ejemplo:

```json
{
    "nombre": "Republica de Chile",
    "nacionalidad": "Chilena",
    "iso_2": "CL",
    "iso_3": "CHL",
    "habilitado": true
}
```

### PATCH - Actualizar parcialmente un país

Permite modificar solamente algunos campos:

```http
PATCH /api/paises/2/
```

Ejemplo:

```json
{
    "nombre": "República de Chile"
}
```

### DELETE - Eliminar un país

Permite eliminar un país mediante su identificador:

```http
DELETE /api/paises/2/
```

---

## Operaciones CRUD

La API implementa las operaciones principales del CRUD:

| Operación               | Método HTTP | Endpoint         |
| ----------------------- | ----------- | ---------------- |
| Listar                  | GET         | `/api/paises/`   |
| Obtener por ID          | GET         | `/api/paises/2/` |
| Crear                   | POST        | `/api/paises/`   |
| Actualizar completo     | PUT         | `/api/paises/2/` |
| Actualizar parcialmente | PATCH       | `/api/paises/2/` |
| Eliminar                | DELETE      | `/api/paises/2/` |

---

## Persistencia

La información registrada mediante la API se almacena en la base de datos MySQL.

Las operaciones realizadas mediante los endpoints modifican directamente los registros almacenados en la base de datos.

---

## requirements.txt

El proyecto contiene el archivo:

requirements.txt

Este archivo contiene las dependencias utilizadas por el proyecto.

Para instalar todas las dependencias:

```bash
pip install -r requirements.txt
```

Para actualizar el archivo después de instalar nuevas dependencias:

```bash
pip freeze > requirements.txt
```

---

## Comprobación del proyecto

Antes de ejecutar o entregar el proyecto se recomienda comprobar su estado mediante:

python manage.py check

También se pueden comprobar las migraciones mediante:

```bash
python manage.py makemigrations --check
```

Si no existen cambios pendientes de migración, el proyecto está preparado para ejecutarse.