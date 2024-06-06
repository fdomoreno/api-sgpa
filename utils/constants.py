import sys
sys.dont_write_bytecode = True

class constants:
    # Constants for the API
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    API = "/api/v1"
    ENV_FILE_PATH = "env.json"
    # Constants for the database
    DB_HOST = "dbhost"
    DB_PORT = "dbport"
    DB_NAME = "dbname"
    DB_USER = "dbuser"
    DB_PASS = "dbpass"
    DB_AUTH ="dbauth_plugin"
    # Constants for the logs
    LOGS = "logs"
    LOGS_PATH = "logpath"
    LOGS_LEVEL = "loglevel"
    LOGS_FILE_NAME = "logfilename"
    LOGS_MAX_BYTES_SIZE = "logmaxsize"
    LOGS_MAX_FILES = "logmaxfiles"

    #Constants Database
    TABLE_USUARIO = "usuario"


    #Constantes de HTTP_CODES AND MESSAGES
    HTTP_200_OK = 200
    HTTP_201_CREATED = 201
    HTTP_204_NO_CONTENT = 204
    HTTP_400_BAD_REQUEST = 400
    HTTP_401_UNAUTHORIZED = 401
    HTTP_404_NOT_FOUND = 404
    HTTP_500_INTERNAL_SERVER_ERROR = 500


    #Constantes de mensajes
    MSG_OK = "OK"
    MSG_CREATED = "Created"
    MSG_NO_CONTENT = "No Content"
    MSG_BAD_REQUEST = "Bad Request"
    MSG_UNAUTHORIZED = "Unauthorized"
    MSG_NOT_FOUND = "Not Found"
    MSG_INTERNAL_SERVER_ERROR = "Internal Server Error"
