from setuptools import setup, find_packages

setup(name="mini_chat_client",
      version="0.0.2",
      description="mini_chat_client",
      author="Evgeniy Sarmanov",
      author_email="esarmanov@noname.com",
      packages=find_packages(),
      install_requires=['Cryptodome.Cipher', 'Cryptodome.PublicKey', 'PyQt5', 'PyQt5.QtCore', 'PyQt5.QtGui',
                        'PyQt5.QtWidgets', 'argparse', 'base64', 'binascii', 'configparser', 'dataclasses', 'datetime',
                        'dis', 'hashlib', 'hmac', 'inspect', 'json', 'logging', 'logs.config_client_log',
                        'logs.config_server_log', 'os', 'socket', 'sqlalchemy', 'sqlalchemy.orm', 'sqlalchemy.sql',
                        'sqlite3', 'sys', 'threading', 'time']
      )

# install_requires = ['PyQt5', 'sqlalchemy', 'pycrypto']

