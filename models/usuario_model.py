from db.db_manager import db_manager
from utils.logger import logger
from datetime import datetime

class usuario_model():
    _cursor = None
    _conexion = None
    _log = logger(__name__).get_logger()

    def __init__(self):
        self._conexion = db_manager().get_connection()
        self._cursor = db_manager().get_cursor()

    def get_usuarios(self):
        try:
            self._cursor.execute("SELECT * FROM usuario")
            self._log.info("Usuarios obtenidos")
            return self._cursor.fetchall()
        except Exception as e:
            self._log.error(f"Error en get_usuarios: {str(e)}")
            raise Exception(f"Error en get_usuarios: {str(e)}")
        
    def get_usuario(self, id_usuario):
        try:
            self._cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
            return self._cursor.fetchone()
        except Exception as e:
            logger.error("Error en get_usuario: " + str(e))
            raise Exception(f"Error en get_usuario: {str(e)}")
        
    def insert_usuario(self, usuario):
        try:
            self._cursor.execute("INSERT INTO usuario (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)", 
                                 (usuario['nombre'], usuario['apellido'], usuario['email'], usuario['password']))
            self._conexion.commit()
            return True
        except Exception as e:
            logger.error("Error en insert_usuario: " + str(e))
            raise Exception(f"Error en insert_usuario: {str(e)}")
        
    def update_usuario(self, usuario):
        try:
            self._cursor.execute("UPDATE usuario SET nombre = %s, apellido = %s, email = %s, password = %s WHERE id_usuario = %s", 
                                 (usuario['nombre'], usuario['apellido'], usuario['email'], usuario['password'], usuario['id_usuario']))
            self._conexion.commit()
            return True
        except Exception as e:
            logger.error("Error en update_usuario: " + str(e))
            raise Exception(f"Error en update_usuario: {str(e)}")
    
    def delete_usuario(self, id_usuario):
        try:
            self._cursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
            self._conexion.commit()
            return True
        except Exception as e:
            logger.error("Error en delete_usuario: " + str(e))
            raise Exception(f"Error en delete_usuario: {str(e)}")
        
    