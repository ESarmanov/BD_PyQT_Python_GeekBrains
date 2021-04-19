import logging
import sys

# Инициализиция логера
# метод определения модуля, источника запуска.
if sys.argv[0].find('client') == -1:
    # если не клиент то сервер!
    logger = logging.getLogger('server')
else:
    # ну, раз не сервер, то клиент
    logger = logging.getLogger('client')


# Дескриптор для описания порта:
class PortValidate:
    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            logger.critical(
                f'Попытка запуска с указанием неподходящего порта {value}. Допустимы адреса с 1024 до 65535.')
            exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class IPValidate:
    def __set__(self, instance, value):
        if len(value) > 0:
            tmp_str = value.split('.')
            if len(tmp_str) != 4:
                SERVER_LOGGER.critical(f"некорректно указан IP адрес: {value}")
                exit(1)
            for el in tmp_str:
                if not el.isdigit():
                    SERVER_LOGGER.critical(f"некорректно указан IP адрес: {value}")
                    exit(1)
                i = int(el)
                if i < 0 or i > 255:
                    SERVER_LOGGER.critical(f"некорректно указан IP адрес: {value}")
                    exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name