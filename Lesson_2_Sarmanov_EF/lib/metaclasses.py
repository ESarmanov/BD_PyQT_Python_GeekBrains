import dis


# Метакласс для проверки соответствия сервера:
class ServerMaker(type):
    def __init__(self, clsname, bases, clsdict):
        # clsname - экземпляр метакласса - Server
        # bases - кортеж базовых классов - ()
        # clsdict - словарь атрибутов и методов экземпляра метакласса

        # Список методов, которые используются в функциях класса:
        methods = []
        # Атрибуты, используемые в функциях классов
        attributes = []
        # перебираем ключи
        for func_element in clsdict:
            # Пробуем
            try:
                # Возвращает итератор по инструкциям в предоставленной функции
                # , методе, строке исходного кода или объекте кода.
                res = dis.get_instructions(clsdict[func_element])
                # Если не функция то ловим исключение
            except TypeError:
                pass
            else:
                # Раз функция разбираем код, получая используемые методы и атрибуты.
                for res_el in res:
                    # print(res_el)
                    # opname - имя для операции
                    if res_el.opname == 'LOAD_GLOBAL':
                        if res_el.argval not in methods:
                            # заполняем список методами, использующимися в функциях класса
                            methods.append(res_el.argval)
                    elif res_el.opname == 'LOAD_ATTR':
                        if res_el.argval not in attributes:
                            # заполняем список атрибутами, использующимися в функциях класса
                            attributes.append(res_el.argval)
        # print(f"attributes={attributes}")
        # print(f"methods={methods}")
        # Если обнаружено использование недопустимого метода connect, бросаем исключение:
        if 'connect'.lower() in methods:
            raise TypeError("Серверный класс не может использовать метод 'connect'")
        # Если сокет не инициализировался функцией create_socket.
        #        if not ('SOCK_STREAM' in attributes and 'AF_INET' in attributes):
        #            raise TypeError('Некорректная инициализация сокета.')
        if not ('socket_transport'.lower() in attributes and 'create_socket'.lower() in methods):
            raise TypeError('Некорректная инициализация сокета.')
        # Обязательно вызываем конструктор предка:
        super().__init__(clsname, bases, clsdict)


# Метакласс для проверки корректности клиентов:
class ClientMaker(type):
    def __init__(self, clsname, bases, clsdict):
        # Список методов, которые используются в функциях класса:
        methods = []
        for func in clsdict:
            # Пробуем
            try:
                res = dis.get_instructions(clsdict[func])
                # Если не функция то ловим исключение
            except TypeError:
                pass
            else:
                # Раз функция разбираем код, получая используемые методы.
                for res_el in res:
                    if res_el.opname == 'LOAD_GLOBAL':
                        if res_el.argval not in methods:
                            methods.append(res_el.argval)

        # Если обнаружено использование недопустимого метода accept, listen, socket бросаем исключение:
        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError('В классе обнаружено использование запрещённого метода')
        # Вызов get_message или send_message из utils считаем корректным использованием сокетов
        if 'get_message' in methods or 'send_message' in methods:
            pass
        else:
            raise TypeError('Отсутствуют вызовы функций, работающих с сокетами.')
        super().__init__(clsname, bases, clsdict)
