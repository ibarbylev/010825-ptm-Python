"""
Пример использования библиотеки PyMySQL

Установка: pip install pymysql
"""

import pymysql
from local_settings import dbconfig


connection = pymysql.connect(**dbconfig)
cursor = connection.cursor()

cursor.execute("SELECT * FROM world.city LIMIT 10")
print(*cursor.fetchall(), sep="\n")

cursor.close()
connection.close()
