#Mysql
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import pooling
from utils.environments import environments
from utils.logger import logger
import os


#Clase singleton que se encarga de la conexión a la base de datos
class db_manager:
    _instancia = None
    _conexion = None
    _cursor = None
    _environment = None
    _log = logger(__name__).get_logger()

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

    def disconnect(self):
        try:
            self._cursor.close()
            self._conexion.close()
            self._log.info("Conexión cerrada")
        except Exception as e:
            self._log.error(f"Error en disconnect: {str(e)}")
            raise Exception(f"Error en disconnect: {str(e)}")
        
    def connect(self):
        try:
            self._conexion = mysql.connector.connect(
                user=self._environment.get('dbuser'),
                password=self._environment.get('dbpass'),
                host=self._environment.get('dbhost'),
                database=self._environment.get('dbname'),
                port=self._environment.get('dbport'),
                auth_plugin=self._environment.get('dbauth_plugin')
            )
            self._cursor = self._conexion.cursor(dictionary=True)
            self._log.info("Conexión establecida")
        except Exception as e:
            self._log.error(f"Error en connect: {str(e)}")
            raise Exception(f"Error en connect: {str(e)}")
        

    def getAll(self, table, fields=None, where=None):
        try:
            if fields is None:
                fields = "*"
            else:
                fields = ",".join(fields)
            sql = f"SELECT {fields} FROM {table}"
            if where is not None:
                sql += f" WHERE {where}"
            if self._cursor is None:
                self.connect()
            self._cursor.execute(sql)
            #Return a list of dictionaries
            result = self._cursor.fetchall()
            self.disconnect()
            return result
        except Exception as e:
            self.disconnect()
            self._log.error(f"Error en getAll: {str(e)}")
            raise Exception(f"Error en getAll: {str(e)}")

