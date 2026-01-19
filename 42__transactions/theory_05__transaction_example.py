"""
Условие задачи:
Продавец получает оплату только если баланс Покупателя >= 0

Сначала продавец получает оплату, затем сумма снимается со счёта покупателя.

Если одна из операций даёт ошибку, то отменяются обе.

Никаких дополнительных проверок в Python-коде: всё проверяется на уровне ограничений таблицы
"""


import mysql.connector
from mysql.connector import Error, DatabaseError
from local_settings import dbconfig_write


def setup_db(dbconfig_write):
    with mysql.connector.connect(**dbconfig_write) as conn:
        with conn.cursor() as cursor:

            # удаляем таблицы, если есть
            cursor.execute("DROP TABLE IF EXISTS CUSTOMER")
            cursor.execute("DROP TABLE IF EXISTS SHOP")
        
            # создаём таблицы покупателя и продавца
            cursor.execute("""
                CREATE TABLE CUSTOMER (
                    amount DECIMAL(10,2) DEFAULT 0,
                    CHECK (amount >= 0)
                )
            """)
        
            cursor.execute("""
                CREATE TABLE SHOP (
                    amount DECIMAL(10,2) DEFAULT 0,
                    CHECK (amount >= 0)
                ) 
            """)
        
            # начальные данные
            cursor.execute("INSERT INTO CUSTOMER (amount) VALUES (100.00)")
            cursor.execute("INSERT INTO SHOP (amount) VALUES (0)")
        conn.commit()
    
    
def get_balances():
    with mysql.connector.connect(**dbconfig_write) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT amount FROM CUSTOMER")
            customer_balance = cursor.fetchone()[0]
            cursor.execute("SELECT amount FROM SHOP")   
            shop_balance = cursor.fetchone()[0]
            print(f"customer amount: {customer_balance}, shop amount: {shop_balance}")


def make_sale(price):
    conn = None
    try:
        conn = mysql.connector.connect(**dbconfig_write)
        conn.autocommit = False  # необязательно, но так читабельнее

        cursor = conn.cursor()

        cursor.execute(
            "UPDATE SHOP SET amount = amount + %s",
            (price,)
        )

        cursor.execute(
            "UPDATE CUSTOMER SET amount = amount - %s",
            (price,)
        )

        conn.commit()
        print("✅ Продажа успешна")

    except DatabaseError as e:
        conn.rollback()
        print("❌ Нарушено ограничение БД:", e.msg)

    except Error as e:
        if conn and conn.is_connected():
            conn.rollback()
        print("❌ Общая ошибка:", e)

    finally:
        if conn and conn.is_connected():
            conn.close()



if __name__ == "__main__":
    # создаём (или пересоздаём) таблицы
    setup_db(dbconfig_write)
    get_balances()

    # успешная продажа
    make_sale(30)
    get_balances()

    # неуспешная продажа (CHECK >= 0)
    make_sale(200)
    get_balances()
