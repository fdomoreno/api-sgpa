#Mysql
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import pooling
from utils.environments import environments
import os


#Clase singleton que se encarga de la conexión a la base de datos
class db_manager:
    _instancia = None
    _conexion = None
    _cursor = None
    _environment = None

    def __new__(self):
        if self._instancia is None:
            self._instancia = object.__new__(self)
            self._instancia._environment = environments().get_env()
            self._instancia._conexion = mysql.connector.connect(
                user=self._instancia._environment.get('dbuser'),
                password=self._instancia._environment.get('dbpass'),
                host=self._instancia._environment.get('dbhost'),
                database=self._instancia._environment.get('dbname'),
                port=self._instancia._environment.get('dbport'),
                auth_plugin=self._instancia._environment.get('dbauth_plugin')
            )
            self._instancia._cursor = self._instancia._conexion.cursor(dictionary=True)
        return self._instancia
    
    def get_cursor(self):
        return self._instancia._cursor
    
    def get_connection(self):
        return self._instancia._conexion
    
    def close(self):
        self._instancia._cursor.close()
        self._instancia._conexion.close()
        self._instancia = None
        self._cursor = None
        self._conexion = None
        self._environment = None

    