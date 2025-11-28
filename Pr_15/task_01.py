"""01 Анализ оценок по кварталам

Реализуйте программу, которая должна:
- прочитать данные из JSON-файла.

Для каждого ученика и предмета вычислить среднюю оценку за каждый учебный квартал:
1 квартал: январь–март
2 квартал: апрель–май (лето пропускается)
3 квартал: сентябрь–декабрь
Записать результаты в новый JSON-файл, сгруппированные по ученикам, предметам и кварталам.
Данные:

Файл grades.json содержит список записей следующего формата:
{"name": "Bob", "subject": "Science", "grade": 86, "date": "06-09-2025"},
  {"name": "Diana", "subject": "Science", "grade": 85, "date": "31-01-2025"},
  {"name": "Bob", "subject": "Literature", "grade": 60, "date": "19-07-2025"},
  {"name": "Charlie", "subject": "Literature", "grade": 78, "date": "05-08-2025"},
  {"name": "Ethan", "subject": "Literature", "grade": 69, "date": "08-04-2025"},
  {"name": "Charlie", "subject": "Science", "grade": 63, "date": "24-10-2025"},
  {"name": "Ethan", "subject": "Math", "grade": 80, "date": "30-01-2025"},
  {"name": "Alice", "subject": "Physics", "grade": 90, "date": "15-09-2025"},
  {"name": "Ethan", "subject": "Science", "grade": 63, "date": "18-09-2025"},
  ...
]
Пример вывода (quarterly_report.json):
{
    "Bob": {
        "Science": {
            "Q1": 86.0
        },
        "Literature": {
            "Q1": 94.0,
            "Q2": 68.0,
            "Q3": 81.0
        },
        "History": {
            "Q1": 73.67
        }
    },
    "Diana": {
        "Science": {
            "Q2": 85.0
        },
        "Physics": {
            "Q2": 92.0,
            "Q3": 72.0
        },
        ...
    },
    ...
}
"""

import json
from datetime import datetime
from collections import defaultdict


def get_quarter(date_str) -> str | None:
    """Определяет квартал по дате."""


def read_grades(file_path="grades.json") -> list[dict]:
    """Читает данные оценок из JSON-файла."""


def calculate_quarterly_averages(data) -> dict:
    """Вычисляет средние оценки по кварталам для каждого ученика и предмета."""
    pass


def save_report(report, file_path="grades_quarterly_report.json") -> None:
    """Сохраняет отчет в JSON-файл."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)


def generate_quarterly_report(input_file="grades.json", output_file="grades_quarterly_report.json") -> None:
    """Главная функция для запуска всего процесса."""
    data = read_grades(input_file)
    report = calculate_quarterly_averages(data)
    save_report(report, output_file)
    print(f"Отчет успешно сохранен в {output_file}")


generate_quarterly_report()

