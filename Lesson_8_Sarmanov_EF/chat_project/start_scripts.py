""" Служебный скрипт запуска/останова нескольких клиентских приложений """
import time
from subprocess import Popen, CREATE_NEW_CONSOLE

p_list = []

while True:
    USER = input("Запустить сервер и клиентов (s) / Закрыть процессы (k) / Выйти (q) ")

    if USER == 'q':
        break

    elif USER == 's':
        p_list.append(Popen('python server.py', creationflags=CREATE_NEW_CONSOLE))
        time.sleep(2)
        p_list.append(Popen('python client.py -n AAA -p a', creationflags=CREATE_NEW_CONSOLE))
        p_list.append(Popen('python client.py -n BBB -p b', creationflags=CREATE_NEW_CONSOLE))
#         p_list.append(Popen('python client.py', creationflags=CREATE_NEW_CONSOLE))
    elif USER == 'k':
        for p in p_list:
            p.kill()
        p_list.clear()

