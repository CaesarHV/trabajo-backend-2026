## Instrucciones de Instalación

### 1. Crear el Ambiente Virtual

Estando ubicados en el directorio principal, iniciamos un nuevo terminal.
Para crear el ambiente virtual, ejecutamos el siguiente comando en el terminal:
  python -m venv cesar

### 2. Activación de Ambiente Virtual

Mediante el terminal accedemos al directorio creado anteriormente, ejecutando el siguiente comando:

  cd nombre_ambiente\Scripts

Para activar el ambiente virtual, ejecutamos el siguiente comando en el terminal:
  .\Activate

Si no se puede ejecutar el comando, debemos darle permisos al terminal, mediante el siguiente comando:
  Set-ExecutionPolicy Bypass -Scope CurrentUser

Habiendo ejecutado este comando, ya deberíamos poder ejecutar el comando anterior y activar nuestro ambiente virtual.

Si necesitamos desactivar el ambiente virtual, usaremos el comando:
  deactivate


### 2. Instalar Dependencias

Ejecutar en la terminal:

  pip install -r requirements.txt

### 3. Ejecutar el Proyecto

Una vez todo listo, ya podemos iniciar el servidor de la aplicación, ejecutando el siguiente comando en el terminal:

  python manage.py runserver

La URL del servidor será: "http://127.0.0.1:8000/"
