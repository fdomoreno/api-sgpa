from models.usuario_model import usuario_model
from utils.logger import logger

class usuario_service():

    _log = logger(__name__)

    def __init__(self):
        pass

    def get_usuarios(self):
        try:
            return usuario_model().get_usuarios()
        except Exception as e:
            self._log.error(f"Error en get_usuarios: {str(e)}")
            raise Exception(f"Error en get_usuarios: {str(e)}")
        
    def get_usuario(self, id_usuario):
        try:
            return usuario_model().get_usuario(id_usuario)
        except Exception as e:
            self._log.error("Error en get_usuario: " + str(e))
            raise Exception(f"Error en get_usuario: {str(e)}") 
        
    def insert_usuario(self, usuario):
        try:
            return usuario_model().insert_usuario(usuario)
        except Exception as e:
            self._log.error("Error en insert_usuario: " + str(e))
            raise Exception(f"Error en insert_usuario: {str(e)}")
    
    def update_usuario(self, usuario):
        try:
            return usuario_model().update_usuario(usuario)
        except Exception as e:
            self._log.error("Error en update_usuario: " + str(e))
            raise Exception(f"Error en update_usuario: {str(e)}")
    