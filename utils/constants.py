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
