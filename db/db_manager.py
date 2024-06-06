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
    
    def connect(self):
        try:
            self._instancia._conexion = mysql.connector.connect(
                user=self._instancia._environment.get('dbuser'),
                password=self._instancia._environment.get('dbpass'),
                host=self._instancia._environment.get('dbhost'),
                database=self._instancia._environment.get('dbname'),
                port=self._instancia._environment.get('dbport'),
                auth_plugin=self._instancia._environment.get('dbauth_plugin')
            )
            self._instancia._cursor = self._instancia._conexion.cursor(dictionary=True)
            self._instancia._log.info("Conexión establecida")
        except Exception as e:
            self._instancia._log.error(f"Error en connect: {str(e)}")
            raise Exception(f"Error en connect: {str(e)}")
    
    def close(self):
        self._instancia._cursor.close()
        self._instancia._conexion.close()
        self._instancia._cursor = None
        self._instancia._conexion = None

    def disconnect(self):
        self._instancia._cursor = None
        self._instancia._conexion = None
        self._instancia._log.info("Conexión cerrada")

    def getAll(self, table, fields=None, where=None):
        try:
            if fields is None:
                fields = "*"
            else:
                fields = ",".join(fields)
            sql = f"SELECT {fields} FROM {table}"
            if where is not None:
                sql += f" WHERE {where}"
            if self._instancia._cursor is None:
                self._instancia._connect()
            self._instancia._cursor.execute(sql)
            result = self._instancia._cursor.fetchall()
            self._instancia.disconnect()
            return result
        except Exception as e:
            self._instancia.disconnect()
            self._instancia._log.error(f"Error en getAll: {str(e)}")
            raise Exception(f"Error en getAll: {str(e)}")
            

    def getById(self, table, id,fields=None):
        try:
            if fields is None:
                fields = "*"
            else:
                fields = ",".join(fields)
            sql = f"SELECT {fields} FROM {table} WHERE id = {id}"
            if self._instancia._cursor is None:
                self._connect()
            self._instancia._cursor.execute(sql)
            result = self._instancia._cursor.fetchone()
            self._instancia.disconnect()
            return result
        except Exception as e:
            self._instancia.disconnect()
            self._instancia._log.error(f"Error en getById: {str(e)}")
            raise Exception(f"Error en getById: {str(e)}")
        
    def insert(self, table, data):
        try:
            fields = ",".join(data.keys())
            values = ",".join([f"'{x}'" for x in data.values()])
            sql = f"INSERT INTO {table} ({fields}) VALUES ({values})"
            if self._instancia._cursor is None:
                self._instancia._connect()
            self._instancia._cursor.execute(sql)
            self._instancia._conexion.commit()
            self._instancia.disconnect()
            return True
        except Exception as e:
            self._instancia.disconnect()
            self._instancia._log.error(f"Error en insert: {str(e)}")
            raise Exception(f"Error en insert: {str(e)}")
    
    def update(self, table, data, id):
        try:
            fields = [f"{k} = '{v}'" for k,v in data.items()]
            sql = f"UPDATE {table} SET {','.join(fields)} WHERE id = {id}"
            if self._instancia._cursor is None:
                self._connect()
            self._instancia._cursor.execute(sql)
            self._instancia._conexion.commit()
            self._instancia.disconnect()
            return True
        except Exception as e:
            self._instancia.disconnect()
            self._instancia._log.error(f"Error en update: {str(e)}")
            raise Exception(f"Error en update: {str(e)}")
        
    def delete(self, table, id):
        try:
            sql = f"DELETE FROM {table} WHERE id = {id}"
            if self._instancia._cursor is None:
                self._connect()
            self._instancia_cursor.execute(sql)
            self._instancia_conexion.commit()
            self._instancia.disconnect()
            return True
        except Exception as e:
            self._instancia.disconnect()
            self._instancia._log.error(f"Error en delete: {str(e)}")
            raise Exception(f"Error en delete: {str(e)}")
        