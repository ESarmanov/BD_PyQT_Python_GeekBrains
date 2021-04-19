from setuptools import setup, find_packages

setup(name="mini_chat_server",
      version="0.0.2",
      description="mini_chat_server",
      author="Evgeniy Sarmanov",
      author_email="esarmanov@noname.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'argparse', 'binascii', 'configparser', 'dataclasses', 'datetime', 'hashlib', 'hmac',
                        'json', 'logging', 'os', 'select', 'socket', 'sqlalchemy', 'sqlalchemy.orm', 'sqlalchemy.sql',
                        'sqlite3', 'sys', 'threading']
      )

# install_requires = ['PyQt5', 'sqlalchemy', 'pycrypto']
