# Turnow Project


API built in Django Rest Framework to cover the backend of this project

1. Create and build the virtual environment in bash console:

```sh
py -m venv venv
source venv/Scripts/activate
```
2. Create requirements.txt
```sh
pip freeze > requirements.txt
```
- Install dependencies:
```sh
pip install -r requirements.txt
```

3. Install Django rest Framework:

```sh
pip install djangorestframework
```
4. Create django project (do not create a new folder):

```sh
django-admin startproject core .
```

5. Create a new app for each database Entity and add it to INSTALLED_APPS in settings.py:
```sh
py manage.py startapp turns
```

6. Try the server:
```sh
py manage.py runserver
```

7. Create a new database in PostgreSQL (PgAdmin), and install the adapter of postgresql for Django:

```sh
pip install psycopg2
```

8. Modify settings.py, update DATABASES:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'TurnowDB',
        'USER': 'postgres',
        'PASSWORD': '', # General postgresql password
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}
```

![Alt text](../img/PostgreSQLServerProps.JPG)

9. Make migrations:

```sh
py manage.py makemigrations
py manage.py migrate
```

10. Create models and serializers in every app.

11. Add the following statement at settings.py:

```sh
AUTH_USER_MODEL = 'users.CustomUser'
```
12. Make migrations, if there is any problem, delete python migrations files and the database.

13. Create a superuser

```sh
py manage.py createsuperuser
```
username: daniel
email: a@a.com
password: abcd9874

username: Cristiano
email: b@b.com
password: qazxsw1234

username: cuadrado
email: b@b.com
password: abcd9874

- Create visualizations for models in panel admin updating admin.py files.

14. Create the views, urls and add 'rest_framework' to INSTALLED_APPS.


## Subiendo a Github

1. Creo nuevo Repo en Github o Gitlab
2. Creo repositorio local en mi carpeta local del proyecto
```sh
git init --initial-branch=main
```
3. Hago mi enlace con el repositorio remoto al que quiero subir el proyecto
```sh
git remote add origin https://github.com/dago-tech/Project_1_Turnow_Backend.git
```
4. Agrego todos los archivos del proyecto al area de stage
```sh
git add .
```
5. Hago commit para enviar mis archivos al repositorio local
```sh
git commit -m "Deploy1"
```
6. Hago push para enviar mi repositorio local al repo remoto
```sh
git push -u origin main
```
- Si obtengo la respuesta:
```
Updates were rejected because the remote contains work that you do
not have locally. This is usually caused by another repository pushing
to the same ref. You may want to first integrate the remote changes
(e.g., 'git pull ...') before pushing again.
See the 'Note about fast-forwards' in 'git push --help' for details.
```
- Este error se debe a que lo que está en el repositorio remoto es diferente a lo del local, así que debo integrarlos. Se recomienta hacer un git pull que traiga el repo remoto hacia el local

- Verifico que el repo remoto sea 'origin' y que me muestre su URL, con:

```sh
git remote
git remote -v
```

- (origin es simplemente el nombre predeterminado que recibe el repositorio remoto principal contra el que trabajamos.)

7. Hago git pull intentando traer lo del repo remoto, en este caso hay error porque los commits del repo local son diferentes a los del repo remoto:

```sh
git pull origin main 
(fatal: refusing to merge unrelated histories)
```
8. Agrego una instruccion adicional a git para permitir historias no relacionadas:
```sh
git pull origin main --allow-unrelated-histories
```
9. Finalmente puedo hacer el push con exito:
```sh
git push origin main
```


## API Schema and documentation Generation

Un Schema es metadata que detalla cómo la data está estructurada. Metadata = data about data.

Para generar el Schema de nuestro proyecto, instalamos:

```sh
pip install PyYAML
```

- En nuestro archivo de urls.py general importamos:
```sh
from rest_framework.schemas import get_schema_view
```

- Y agregamos una ruta:

```py
path('schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0"
    ), name='openapi-schema'),
```

Ademas, debemos instalar:

```sh
pip install uritemplate
```
- Ahora en la ruta /schema podemos visualizar el schema de nuestro proyecto.

![Alt text](img/Schema1.jpg)


### Doc Generator for Django Rest Framework

- Django Rest Swagger
- Swagger-ui
- drf-yasg
- Redoc

En este caso vamos a generar nuestra documentacion en Swagger-ui, así que importamos lo siguiente en urls.py general:
```py
from rest_framework.documentation import include_docs_urls
```

Agregamos el path:

```py
path('docs/', include_docs_urls(title='BlogAPI')),
```
- Y también debemos instalar coreapi
```sh
pip install coreapi
```
'coreapi' es una herramienta versátil que se utiliza para interactuar con APIs web basadas en documentación interactiva, explorar rutas de API, realizar pruebas de API y generar documentación. En el contexto de Django, coreapi se usa como parte de Django REST framework para mejorar la documentación y la interacción con las APIs web creadas con esta biblioteca.

- En el archivo settings.py agregamos:

```py
REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }
```

- Ahora tenemos con el link /docs la documentacion con la cual podemos interactuar con la API


## CORS

- Instalamos la libreria django-cors-headers, esto permite solicitudes de navegador desde otros origenes.

```sh
pip install django-cors-headers
```

- En el archivo settings.py agregamos corsheaders a las INSTALLED APPS, agregamos el middleware y los origenes colocando la palabra localhost ya que cuando accedemos por el navegador a la app de react, este muestra localhost y no 127.0.0.1: 

```py
"corsheaders.middleware.CorsMiddleware",

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:5173",
]
```

- A este punto ya podemos visualizar los datos de la API en la aplicación de React.


## JWT Authentication

- A token blacklist is created to not allow a refresh token to be used again, when a logout is performed, the refresh token is sent to the blacklist

---

## HTTPS y certificado SSL en local

- Install chocolatey en powershell:

```sh
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```


__Step 1__ - Generating a local SSL certificate
First, let's install mkcert on your machine. If you are running on macOS, you can use Homebrew package manager to do this. Run the following command in your terminal:

```sh
choco install mkcert
```

Next, let's make your Operational System trust the local certificates we're about to generate. You need to install a local certificate authority (CA) in the system trust store to do this. Run the following command:
```sh
mkcert -install
```
Next, you need to generate a certificate for the localhost domain.

In the terminal, go to the root of your Django project. Then run the following terminal command to generate a certificate for localhost and 127.0.0.1:
```sh
mkcert localhost
```

- Instalar Nginx para Windows:

Descarga la versión para Windows de Nginx desde nginx.org.
Descomprime el archivo descargado en una ubicación de tu elección.

- Colocar los dos archivos de certificados en la misma carpeta del nginx.conf

- El nginx.conf establecerlo así:

```sh
events {
    worker_connections 1024;  # Puedes ajustar este número según tus necesidades.
}
http {
    server {
        listen 443 ssl;
        server_name localhost;

        ssl_certificate localhost.pem;
        ssl_certificate_key localhost-key.pem;

        location / {
            proxy_pass http://127.0.0.1:8000;  # El puerto donde Daphne está escuchando
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_redirect off;
        }
    }
}
```
- Agregar nginx al PATH de las variables de entorno de windows colocando su ruta.
- Ejecutar nginx.exe para que se inicie nginx en segundo plano
```sh
start nginx
```
```sh
nginx -s stop
```

And that's it; you should now see the local development server running at the default https://localhost address.

- Mientras el servidor de nginx esté corriendo la app de Django se va a poder correr con el servidor de desarrollo py manage.py runserver y la app va a estar accesible desde https://localhost.

