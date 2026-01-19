dividend = 100

try:
    divisor = int(input("Введите делитель: "))
    if divisor == 0:
        raise ZeroDivisionError("Ошибка: Деление на ноль запрещено!")

    result = dividend / divisor
    print(f"Результат: {result}")

except ValueError as e:
    print(f"{e}")

except ZeroDivisionError as e:
    print(e)
