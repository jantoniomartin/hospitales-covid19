Cómo importar datos desde un fichero CSV
========================================

Hospitales
----------

Primero, crear un fichero csv con el siguiente formato:

- Una línea por cada hospital que se quiera importar
- Campos separados por comas
- Textos entre comillas dobles, si es necesario

Orden de campos:

.. code-block::

    teléfono,nombre,localidad,dirección

Ejemplo:

.. code-block::

    914 538 300,Central de la Cruz Roja San José y Santa Adela,Madrid,"Avda. Reina Victoria, 22-26"

Ejecutar el siguiente comando en la consola, con los datos apropiados:

.. code-block::

    python manage.py import_region <region> <archivo.csv>
