"""
Мы можем изменить вывод результата: сделать dict вместо tuple.
Для этого при создании курсора параметр dictionary устанавливаем в True.
"""
from pprint import pprint

import mysql.connector
from local_settings import dbconfig


dbconfig['database'] = 'hr'  # меняем имя дефолтной БД на `hr`

conn = mysql.connector.connect(**dbconfig)


# cursor = conn.cursor(dictionary=False)
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT * FROM employees LIMIT 1")
row = cursor.fetchone()

pprint(row)

# {'employee_id': 100, 'first_name': 'Steven', ...}
# {'commission_pct': None,
#  'department_id': Decimal('90'),
#  'email': 'SKING',
#  'employee_id': Decimal('100'),
#  'first_name': 'Steven',
#  'hire_date': datetime.date(2016, 6, 4),
#  'job_id': 'AD_PRES',
#  'last_name': 'King',
#  'manager_id': None,
#  'phone_NUMERIC': '515.123.4567',
#  'salary': Decimal('24000.00')}


# ===============================  Если dictionary=False  ====================================

# (Decimal('100'),
#  'Steven',
#  'King',
#  'SKING',
#  '515.123.4567',
#  'AD_PRES',
#  Decimal('24000.00'),
#  None,
#  None,
#  Decimal('90'),
#  datetime.date(2016, 6, 4))