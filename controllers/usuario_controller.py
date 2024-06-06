from flask import Blueprint, request, jsonify
from utils.logger import logger
from utils.environments import environments
from utils.constants import constants
from services.usuario_service import usuario_service
from models.contracts.error import error

usuario_controller = Blueprint('usuario_controller', __name__)

logger = logger(__name__)

@usuario_controller.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        return usuario_service().get_usuarios(request.headers.get('Authorization'))
    except Exception as e:
        logger.error(f"Error en get_usuarios: {str(e)}")
        return jsonify(error(constants.HTTP_500_INTERNAL_SERVER_ERROR, constants.MSG_INTERNAL_SERVER_ERROR, str(e)).to_dict()), constants.HTTP_500_INTERNAL_SERVER_ERROR

@usuario_controller.route('/usuario/<id_usuario>', methods=['GET'])
def get_usuario(id_usuario):
    try:
        return jsonify(usuario_service().get_usuario(id_usuario))
    except Exception as e:
        logger.error("Error en get_usuario: " + str(e))
        return jsonify(None)
    
@usuario_controller.route('/usuario', methods=['POST'])
def insert_usuario():
    try:
        return jsonify(usuario_service().insert_usuario(request.json))
    except Exception as e:
        logger.error("Error en insert_usuario: " + str(e))
        return jsonify(False)
    
@usuario_controller.route('/usuario', methods=['PUT'])
def update_usuario():
    try:
        return jsonify(usuario_service().update_usuario(request.json))
    except Exception as e:
        logger.error("Error en update_usuario: " + str(e))
        return jsonify(False)

@usuario_controller.route('/usuario/<id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    try:
        return jsonify(usuario_service().delete_usuario(id_usuario))
    except Exception as e:
        logger.error("Error en delete_usuario: " + str(e))
        return jsonify(False)

