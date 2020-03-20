# hospitales-covid19
Gestión de necesidades de material de hospitales para la emergencia del COVID-19.

Esta aplicación ha sido desarrollada muy deprisa e intentando tener la funcionalidad lo antes posible, por lo que
no todo está hecho de la mejor forma, y puede fallar.

La aplicación está desarrollada sobre el framework Django: https://docs.djangoprojects.com

## Configurar el entorno de desarrollo

### Paso 1. Crearse un entorno virtual (usando virtualenvwrapper)

```
mkvirtualenv hospitales-covid19
```

### Paso 2. Instalar los requirements

```
pip install -r requirements/base.txt
```

### Paso 3. Añadir configuración local

Crear el fichero `settings.py` en el directorio `fuckcovid` con el siguiente contenido:

```python
from config.settings.local import *
SECRET_KEY="tu-clave-secreta"
```

### Paso 4. Crear la BBDD (por defecto estamos usando SQLITE para desarrollo)

```
python manage.py migrate
```

### Paso 5. Cargar los datos de prueba


```
python manage sampledatafiller
```

### Paso 6. Ejecutar el entorno

Por último iniciamos nuestra aplicación ejecutando:

```
python manage runserver
```
