"""
.close() - метод, который:
    - прекращает работу генератора
    - и возвращает исключение StopIteration
    - в самом генераторе вызывает исключение GeneratorExit
"""

# Генераторная функция
def infinite_numbers(start=0, step=1):
    try:
        n = start
        while True:
            yield n
            n += step
    except GeneratorExit as e:
        print(f"{e.__class__.__name__}: {e}")


# Создание генератора
gen = infinite_numbers(0, 1)


# Закрытие генератора с помощью метода close()
while True:
    try:
        n = next(gen)
        print(n)
        if n >= 10:
            gen.close()
    except StopIteration:
        print("Завершение по StopIteration")
        break