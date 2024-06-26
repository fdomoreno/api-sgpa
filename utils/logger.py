'''
 Clase Singleton que se encarga de la configuración y manejo de logs
'''
import logging
import sys
from utils.constants import constants
from utils.environments import environments
sys.dont_write_bytecode = True

class logger:
    _logger = None
    #Que no sea singleton
    def __init__(self, logger='api-sga', log_path=None, log_level=logging.INFO):
        self._logger = logging.getLogger(logger)
        self._logger.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        if log_path is None:
            log_path = environments().get(constants.LOGS).get(constants.LOGS_PATH)
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)


    def get_logger(self):
        return self._logger
    
    def info(self, message:str):
        self._logger.info(message)

    def debug(self, message):
        self._logger.debug(message)

    def error(self, message):
        print(message)
        self._logger.error(message)
    
    def warning(self, message):
        self._logger.warning(message)

    def critical(self, message):
        self._logger.critical(message)

    def exception(self, message):
        self._logger.exception(message)