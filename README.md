Para configuración de Base de datos:

Utilizar MySQL versión 8.0

Ejecutar el archivo: `proyecto_ecosistema_mysql_sin_relaciones.sql` para crear la base de datos y las tablas necesarias.

Para ejecutar un archivo de Python, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando el siguiente comando en tu terminal:

    ```
    python --version
    ```

    Si no tienes Python instalado, puedes descargarlo e instalarlo desde el sitio web oficial de Python.

2. Crear o activar el entorno virtual

    ```
        python -m venv venv
        source venv/bin/activate
    ```

3. Instalar dependencias

    ```
        pip install -r requirements.txt
    ```
4. Configurar variables de entorno tomar como ejemplo archivo .env.example

    ```
        cp env-example.json env.json
    ```


5. Abre tu terminal y navega hasta la ubicación del archivo Python que deseas ejecutar. Puedes usar el comando `cd` para cambiar de directorio.

6. Una vez que estés en el directorio correcto, ejecuta el siguiente comando para ejecutar el archivo Python:

    ```
    python app.py
    ```

    Asegúrate de reemplazar "app.py" con el nombre real de tu archivo Python.

7. Si todo está configurado correctamente, el archivo Python se ejecutará y verás la salida en tu terminal.

Recuerda que estos pasos pueden variar dependiendo del sistema operativo que estés utilizando. Asegúrate de tener los permisos adecuados para ejecutar el archivo y de que todas las dependencias necesarias estén instaladas. 


## Información técnica:

- Base de datos: MySQL
- Versión de Python: 3.10.11

## Prueba con Postman:

1. Abre Postman y importar colecció de pruebas `Talento_Tech_G1.postman_collection.json`.
2. Verificar las cabeceras de usuario y contraseña en la colección.
3. Ejecutar las pruebas.