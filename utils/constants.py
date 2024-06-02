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
    LOGS_MAX_FILE = "logmaxfiles"

    #Database
    TABLE_USUARIO = "usuario"

    


    #HTTP Status
    HTTP_OK = 200
    HTTP_MESSAGE_OK = "OK"
    HTTP_CREATED = 201
    HTTP_MESSAGE_CREATED = "Created"
    HTTP_BAD_REQUEST = 400
    HTTP_MESSAGE_BAD_REQUEST = "Bad Request"
    HTTP_UNAUTHORIZED = 401
    HTTP_MESSAGE_UNAUTHORIZED = "Unauthorized"
    HTTP_FORBIDDEN = 403
    HTTP_MESSAGE_FORBIDDEN = "Forbidden"
    HTTP_NOT_FOUND = 404
    HTTP_MESSAGE_NOT_FOUND = "Not Found"
    HTTP_INTERNAL_SERVER_ERROR = 500
    HTTP_MESSAGE_INTERNAL_SERVER_ERROR = "Internal Server Error"
