'''
 Clase Singleton que se encarga de la configuración y manejo de logs
'''
import logging
import sys
sys.dont_write_bytecode = True

class logger:
    _instance = None
    _logger = None

    def __new__(self, logger='api-sga', log_path=None, log_level=logging.INFO):
        if self._instance is None:
            self._instance = object.__new__(self)
            self._instance._logger = logging.getLogger(logger)
            self._instance._logger.setLevel(log_level)
            if log_path is not None:
                file_handler = logging.FileHandler(log_path)
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                file_handler.setFormatter(formatter)
                self._instance._logger.addHandler(file_handler)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self._instance._logger.addHandler(console_handler)
        return self._instance

    def get_logger(self):
        return self._instance._logger
    
    def info(self, message:str):
        self._instance._logger.info(message)

    def debug(self, message):
        self._instance._logger.debug(message)

    def error(self, message):
        print(message)
        self._instance._logger.error(message)
    
    def warning(self, message):
        self._instance._logger.warning(message)

    def critical(self, message):
        self._instance._logger.critical(message)

    def exception(self, message):
        self._instance._logger.exception(message)