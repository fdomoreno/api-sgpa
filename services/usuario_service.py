from models.usuario_model import usuario_model
from utils.logger import logger
from flask import jsonify
from utils.constants import constants
from utils.tools import tools
from models.contracts.response import response

class usuario_service():

    _log = logger(__name__)

    def __init__(self):
        pass

    def get_usuarios(self, authorization:str):
        try:
            #Auth basic
            if authorization is None:
                return jsonify(response(constants.HTTP_401_UNAUTHORIZED,constants.MSG_UNAUTHORIZED, None).to_dict()), constants.HTTP_401_UNAUTHORIZED
            #validar basic auth
            if not tools().validar_basic_auth(authorization):
                return jsonify(response(constants.HTTP_401_UNAUTHORIZED,constants.MSG_UNAUTHORIZED, None).to_dict()), constants.HTTP_401_UNAUTHORIZED
            result = usuario_model().get_usuarios()
            self._log.info(f"Usuarios: {result}")
            if result is None or len(result) == 0:
                return jsonify(response(constants.HTTP_404_NOT_FOUND,constants.MSG_NOT_FOUND, {}).to_dict()), constants.HTTP_404_NOT_FOUND
            return jsonify(response(constants.HTTP_200_OK,constants.MSG_OK, result).to_dict()), constants.HTTP_200_OK
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
    
    def delete_usuario(self, id_usuario):
        try:
            return usuario_model().delete_usuario(id_usuario)
        except Exception as e:
            self._log.error("Error en delete_usuario: " + str(e))
            raise Exception(f"Error en delete_usuario: {str(e)}")