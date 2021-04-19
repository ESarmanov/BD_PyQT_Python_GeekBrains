import logging

DEFAULT_PORT = 7777
DEFAULT_IP_ADDRESS = '192.168.1.125'
MAX_CONNECTIONS = 5
PACKAGE_LENGTH = 1024
ENCODING = 'utf-8'
LOGGING_LEVEL = logging.DEBUG
#LOGGING_LEVEL = logging.info()
SERVER_DATABASE = 'sqlite:///server_db.db3'
SERVER_CONFIG = 'server.ini'
SERVER_TIMEOUT = 1/2
POOL_RECYCLE = 7200

# маска разрешенных символов валидаторов полей
# https://habr.com/ru/post/123845/
RE_LOGIN_MASK='[a-zA-Z][a-zA-Z0-9]{1,25}'
RE_PASWD_MASK='[a-zA-Z][a-zA-Z0-9]{1,12}'
RE_IPV4_VALIDATOR='((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)'
RE_IPV6_VALIDATOR='((^|:)([0-9a-fA-F]{0,4})){1,8}$'
RE_PORT_VALIDATOR='[0-9]{0,5}'


CLIENT_LISTEN = False  # используется для определения, клиент пишет или слушает

# Прококол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'from'
DESTINATION = 'to'
DATA = 'bin'
PUBLIC_KEY = 'pubkey'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
EXIT = 'exit'
LISTEN = 'listen'  # ключ для словаря, отправка от клиента запрос на прослушивание
GET_CONTACTS = 'get_contacts'
LIST_INFO = 'data_list'
REMOVE_CONTACT = 'remove'
ADD_CONTACT = 'add'
USERS_REQUEST = 'get_users'
PUBLIC_KEY_REQUEST = 'pubkey_need'

# Словари - ответы:
RESPONSE_200 = {RESPONSE: 200}
RESPONSE_202 = {RESPONSE: 202, LIST_INFO: None}
RESPONSE_400 = {RESPONSE: 400, ERROR: None}
RESPONSE_205 = {RESPONSE: 205}
RESPONSE_511 = {RESPONSE: 511,DATA: None}

