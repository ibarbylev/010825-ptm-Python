"""
Пример использования библиотеки mysqlclient (MySQLdb)

Установка на Linux:

1. Прежде всего требуется установка системных пакетов:

sudo apt update
sudo apt install -y \
    build-essential \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config

2. И только уже затем, установка самой библиотеки:

pip install mysqlclient
"""

import MySQLdb
from local_settings import dbconfig


connection = MySQLdb.connect(**dbconfig)
cursor = connection.cursor()

cursor.execute("SELECT * FROM world.city LIMIT 10")
print(*cursor.fetchall(), sep="\n")

cursor.close()
connection.close()
