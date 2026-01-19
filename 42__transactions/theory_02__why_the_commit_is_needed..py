"""
Зачем нужен метод .commit()

В примере ниже мы:
1. Убираем БД по умолчанию
2. Подключаемся для записи
3. Новую таблицу
    - создаём
    - заполняем
    - проверяем содержимое
4. Отключаемся от БД
5. Снова подключаемся и проверяем содержимое таблицы
"""

import mysql.connector
from local_settings import dbconfig_write

# 1. Убираем БД из подключения, иначе mysql не позволит её удалить
DATABASE = dbconfig_write['database']
dbconfig_write['database'] = None

# 2. Подключаемся для записи
with mysql.connector.connect(**dbconfig_write) as conn:
    with conn.cursor() as cursor:

        # Удаляем БД, чтобы гарантировать, что она пустая
        cursor.execute(f"DROP DATABASE IF EXISTS {DATABASE}")
        cursor.execute(f"CREATE DATABASE {DATABASE}")

        cursor.execute(f"USE {DATABASE}")

        # 3.1. создаём БД
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100),
                quantity INT,
                price DECIMAL(10, 2),
                sale_date DATE
            )
        """)

        # 3.2. Заполняем её значениями
        rows = [
            ("Keyboard", 2, 45.50, "2024-06-15"),
            ("Mouse", 5, 20.00, "2024-06-16"),
            ("Monitor", 1, 150.00, "2024-06-17"),
            ("USB Cable", 10, 5.50, "2024-06-18"),
            ("Webcam", 3, 70.00, "2024-06-19"),
        ]

        cursor.executemany(
            "INSERT INTO sales (item_name, quantity, price, sale_date) VALUES (%s, %s, %s, %s)",
            rows
        )

        # 3.3. проверяем содержимое таблицы
        cursor.execute("SELECT * FROM sales")
        for row in cursor.fetchall():
            print(row)

    # conn.commit()

# 4. Отключаемся от БД
print("=== Закрываем подключение и проверяем содержимое таблицы снова ===")

with mysql.connector.connect(**dbconfig_write) as conn:
    with conn.cursor() as cursor:

        cursor.execute(f"USE {DATABASE}")

        # 5, Снова подключаемся и проверяем содержимое таблицы
        cursor.execute("SELECT * FROM sales")
        for row in cursor.fetchall():
            print(row)


print("\n=== Раскоммичиваем commit и проверяем ещё раз ===")
