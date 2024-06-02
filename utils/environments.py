import os
import json
import sys
from utils.constants import constants
sys.dont_write_bytecode = True

#Clase singleton que se encarga de leer las variables de entorno del archivo env.json
class environments:
    _instance = None
    _env = None

    def __new__(self, env_path=None):
        if self._instance is None:
            self._instance = object.__new__(self)
            self._instance._env = {}
            if env_path is not None:
                self._instance._env = self._instance._load_env(env_path)
            else:
                self._instance._env = self._instance._load_env(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), constants.ENV_FILE_PATH))
        return self._instance

    def _load_env(self, env_path):
        try:
            with open(env_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def get_env(self):
        return self._instance._env

    def get(self, key):
        return self._instance._env.get(key, None)