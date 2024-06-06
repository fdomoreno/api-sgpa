from db.db_manager import db_manager
from utils.logger import logger
from datetime import datetime
from utils.constants import constants

class usuario_model():
    _database = None
    _log = logger(__name__).get_logger()

    def __init__(self):
        self._database = db_manager()

    def get_usuarios(self):
        try:
            return self._database.getAll(constants.TABLE_USUARIO, ["id","nombreusuario","fecha_creacion","fecha_actualizacion"])
        except Exception as e:
            self._log.error(f"Error en get_usuarios: {str(e)}")
            raise Exception(f"Error en get_usuarios: {str(e)}")
        
    def get_usuario(self, id_usuario):
        try:
            return self._database.getById(constants.TABLE_USUARIO, id_usuario, ["id","nombreusuario","fecha_creacion","fecha_actualizacion"])
        except Exception as e:
            logger.error("Error en get_usuario: " + str(e))
            raise Exception(f"Error en get_usuario: {str(e)}")
        
    def insert_usuario(self, usuario):
        try:
           return self._database.insert(constants.TABLE_USUARIO, usuario)
        except Exception as e:
            logger.error("Error en insert_usuario: " + str(e))
            raise Exception(f"Error en insert_usuario: {str(e)}")
        
    def update_usuario(self, usuario):
        try:
            return self._database.update(constants.TABLE_USUARIO, usuario, usuario.get("id"))
        except Exception as e:
            logger.error("Error en update_usuario: " + str(e))
            raise Exception(f"Error en update_usuario: {str(e)}")
    
    def delete_usuario(self, id_usuario):
        try:
            return self._database.delete(constants.TABLE_USUARIO, id_usuario)
        except Exception as e:
            logger.error("Error en delete_usuario: " + str(e))
            raise Exception(f"Error en delete_usuario: {str(e)}")
        
    