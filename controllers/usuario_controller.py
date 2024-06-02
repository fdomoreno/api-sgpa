from flask import Blueprint, request, jsonify
from utils.logger import logger
from utils.environments import environments
from utils.constants import constants
from services.usuario_service import usuario_service
from models.contracts.response import response

usuario_controller = Blueprint('usuario_controller', __name__)

logger = logger(__name__)

@usuario_controller.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        return usuario_service().get_usuarios()
    except Exception as e:
        logger.error(f"Error en get_usuarios: {str(e)}")
        return jsonify(response(constants.HTTP_FORBIDDEN,constants.HTTP_MESSAGE_FORBIDDEN,str(e))),constants.HTTP_FORBIDDEN

@usuario_controller.route('/usuario/<id_usuario>', methods=['GET'])
def get_usuario(id_usuario):
    try:
        return jsonify(usuario_service().get_usuario(id_usuario))
    except Exception as e:
        logger.error("Error en get_usuario: " + str(e))
        return jsonify(response(constants.HTTP_FORBIDDEN,constants.HTTP_MESSAGE_FORBIDDEN,str(e))),constants.HTTP_FORBIDDEN
    
@usuario_controller.route('/usuario', methods=['POST'])
def insert_usuario():
    try:
        return jsonify(usuario_service().insert_usuario(request.json))
    except Exception as e:
        logger.error("Error en insert_usuario: " + str(e))
        return jsonify(response(constants.HTTP_FORBIDDEN,constants.HTTP_MESSAGE_FORBIDDEN,str(e))),constants.HTTP_FORBIDDEN
    
@usuario_controller.route('/usuario', methods=['PUT'])
def update_usuario():
    try:
        return jsonify(usuario_service().update_usuario(request.json))
    except Exception as e:
        logger.error("Error en update_usuario: " + str(e))
        return jsonify(response(constants.HTTP_FORBIDDEN,constants.HTTP_MESSAGE_FORBIDDEN,str(e))),constants.HTTP_FORBIDDEN

@usuario_controller.route('/usuario/<id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    try:
        return jsonify(usuario_service().delete_usuario(id_usuario))
    except Exception as e:
        logger.error("Error en delete_usuario: " + str(e))
        return jsonify(response(constants.HTTP_FORBIDDEN,constants.HTTP_MESSAGE_FORBIDDEN,str(e))),constants.HTTP_FORBIDDEN

