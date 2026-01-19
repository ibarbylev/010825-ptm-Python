# Генераторная функция
def infinite_numbers(start=0, step=1):
    n = start
    while True:
        yield n
        n += step


# Создание генератора
gen = infinite_numbers(0, 1)


# Запуск генератора
for x in gen:
    print(x)   # будет выводить 0,1

    # обязательное условие для бесконечного генератора
    if x >= 10:
        break