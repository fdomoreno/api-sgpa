from flask import Flask
from utils.constants import constants
import sys

sys.dont_write_bytecode = True

def create_app():
    app = Flask(__name__)

    from controllers.usuario_controller import usuario_controller

    app.register_blueprint(usuario_controller, url_prefix=constants.API)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5001, debug=True)
