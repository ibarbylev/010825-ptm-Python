import unittest
import mysql.connector
from mysql.connector.errors import ProgrammingError
from local_settings import dbconfig



def get_10_rows_from_table(cursor, table_name):
    query = f"SELECT * FROM {table_name} LIMIT 10"
    cursor.execute(query)
    return cursor.fetchall()


class Test1MySQLDatabase(unittest.TestCase):

    def setUp(self):
        """Подключение к БД перед каждым тестом"""
        self.conn = mysql.connector.connect(**dbconfig)
        self.cursor = self.conn.cursor()

    def tearDown(self):
        """Закрытие соединения после каждого теста"""
        self.cursor.close()
        self.conn.close()

    def test_connection(self):
        """Проверка соединения с БД"""
        self.cursor.execute("SELECT 1;")
        result = self.cursor.fetchone()

        self.assertEqual(result[0], 1)

    def test_get_10_rows_from_table(self):
        """Проверка получения 10 строк из таблицы"""
        rows = get_10_rows_from_table(self.cursor, "country")

        self.assertIsInstance(rows, list)
        self.assertEqual(len(rows), 10)

    def test_raise_exception(self):
        """Проверка вызова исключения на ошибочное имя таблицы"""
        with self.assertRaises(ProgrammingError):
            get_10_rows_from_table(self.cursor, "countr")