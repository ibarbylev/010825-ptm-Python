"""Практические задания 13
Лекция 26 - Работа с файловой системой

Анализ продаж по категориям и датам

Напишите программу, которая обрабатывает текстовый файл с данными о продажах.
Используйте файл sales_data.txt.

Программа должна:

1. Принимать аргументы командной строки:
python sales_report.py <input_file> <output_directory>
Где:
<input_file> — путь к входному файлу с продажами.
<output_directory> — папка, куда будут сохранены отчёты.

2. Считать данные из текстового файла,
в котором каждая строка содержит информацию в следующем формате:

имя,дата,сумма,категория,город

Пример входных данных:
Olivia Suarez,2024-08-02,4565,Electronics,Dallas
Jennifer Jacobs,2023-08-19,4963,Automotive,London
Erin Johnson,2024-08-29,1796,Clothing,Miami


3. Сгруппировать данные по годам и месяцам,
создавая для каждого года и месяца отдельную папку в указанной директории.


4. Создать общий отчёт по каждому месяцу (monthly_report.txt),
в котором указана
- суммарная выручка по каждой категории
- и общая сумма:

Automotive,109539
Books,133160
Clothing,102001
Electronics,79403
Groceries,104387
Home Appliances,99911
Sports,78782
Full,707183

5. Создать файлы для каждой категории товаров,
в которых должны быть указаны все продажи по данной категории в формате:

дата,имя продавца,сумма

Пример файла Electronics.txt:
2025-02-01,Cynthia Maddox,538
2025-02-01,Kendra Martinez,3799
2025-02-02,Rachel Miller,1097

Все записи в файле должны быть отсортированы по дате.

Пример запуска программы

python sales_report.py sales_data.txt reports

Пример созданной структуры
reports/
├── 2024/
│   ├── 12/
│   │   ├── monthly_report.txt
│   │   ├── Automotive.txt
├── 2025/
│   ├── 01/
│   │   ├── monthly_report.txt
│   │   ├── Clothing.txt
│   │   ├── Electronics.txt
│   ├── 02/
│   │   ├── monthly_report.txt
│   │   ├── Groceries.txt
│   │   ├── Sports.txt
"""

import os
import sys
from pprint import pprint


def process_sales_data(file_path, output_dir):
    """Обрабатывает продажи и создаёт отчёты по категориям и общие отчёты по месяцам."""
    """Обрабатывает продажи и создаёт отчёты по категориям и общие отчёты по месяцам."""
    """    
    grouped_sales ==================================================
    {   
        ('2023', '07', 'Beauty'): [{'amount': 3724,
                                 'category': 'Beauty',
                                 'date': '2023-07-28',
                                 'month': '07',
                                 'name': 'Elena Bell',
                                 'year': '2023'},
                                {'amount': 1975,
                                 'category': 'Beauty',
                                 'date': '2023-07-06',
                                 'month': '07',
                                 'name': 'Aria Bryant',
                                 'year': '2023'}],
        ('2023', '07', 'Clothing'): [{'amount': 1842,
                                   'category': 'Clothing',
                                   'date': '2023-07-23',
                                   'month': '07',
                                   'name': 'Mia Thomas',
                                   'year': '2023'}],
    ...
    }

    category_totals ==================================================
    {
        ('2023', '07'): {'Beauty': 5699,
                          'Clothing': 1842,
                          'Electronics': 8338,
                          'Toys': 15223},
        ('2023', '08'): {'Automotive': 15017, 'Books': 6587, 'Sports': 11370},
        ('2023', '09'): {'Automotive': 9287,
                          'Beauty': 2384,
                          'Books': 4210,
                          'Clothing': 6399,
                          'Sports': 14115},
        ('2023', '10'): {'Books': 9606, 'Clothing': 4895, 'Electronics': 4141},
    }
    """
    pass


def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file> <output_directory>")
        return

    input_file = sys.argv[1]
    output_directory = sys.argv[2]

    process_sales_data(input_file, output_directory)
    pprint("Reports generated successfully!")


# python task.py sales_data.txt data
if __name__ == "__main__":
    main()