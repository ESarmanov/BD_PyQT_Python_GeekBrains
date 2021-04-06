import json
import sys
import socket
sys.path.append('../')
from lib.variables import *
from lib.errors import *
from logs.decoration_log import log


@log
def get_message(client):
    encoded_response = client.recv(PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataRecivedError
    else:
        raise IncorrectDataRecivedError

@log
def send_message(sock, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)


def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Проверка что строка является действительным адресом IPv4.
def validate_ip(ip_str):
    tmp_str = ip_str.split('.')
    if len(tmp_str) != 4:
        return False
    for el in tmp_str:
        if not el.isdigit():
            return False
        i = int(el)
        if i < 0 or i > 255:
            return False
    return True

# Проверка что строка может являться разрешенным портом
def validate_port(ip_port):
    try:
        ip_port = int(ip_port)
        if ip_port < 1025 or ip_port > 65535:
            return False
        else:
            return True
    except:
        return False


def server_settings():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    server.py -i(or -ip) 192.168.1.125 -p(or -port) 9999
    :return:
    '''
    client_listen = CLIENT_LISTEN
    try:
        # ищем в строке запуска тип клиента -l(listen) для клиентов, которые будут в роли "слушателя"
        # print("-l", sys.argv)
        if '-l' in sys.argv:
            # print("client_listen=====True")
            client_listen = True

        # ищем в строке запуска ip
        if '-ip' in sys.argv:
            server_address = sys.argv[sys.argv.index('-ip') + 1]
        elif '-i' in sys.argv:
            server_address = sys.argv[sys.argv.index('-i') + 1]
        else:
            server_address = DEFAULT_IP_ADDRESS
        # if not validate_ip(server_address) and server_address != '':
        #    raise ValueError

        # ищем в строке запуска порт
        if '-p' in sys.argv:
            server_port = int(sys.argv[sys.argv.index('-p') + 1])
        elif '-port' in sys.argv:
            server_port = int(sys.argv[sys.argv.index('-port') + 1])
        else:
            server_port = DEFAULT_PORT
        # if not validate_port(server_port):
        #    raise ValueError

    except ValueError:
        print('Некорректный адрес. Запуск скрипта должен быть: ****.py -i(or -ip) XXX.XXX.XXX.XXX -p(or -port) 9999')
        sys.exit(1)
    return [server_address, server_port, client_listen]

