"""С помощью замыкания создаём функцию с нужными множителем"""

def multiplier(a):
    def inner(b):
        return a * b
    return inner


multiply_by_2 = multiplier(2)
multiply_by_3 = multiplier(3)

print(multiply_by_2(5))
print(multiply_by_3(5))

# 10
# 15

""" ============= Счётчик запуска функций =============="""

def counter(count=0):
    def inner():
        nonlocal count
        count += 1
        print(f"Функция запускается в {count}-й раз")
    return inner


run_counter = counter()

run_counter()
run_counter()
run_counter()

# Функция запускается в 1-й раз
# Функция запускается в 2-й раз
# Функция запускается в 3-й раз


""" ======= Сохранение параметров функций в списке ========"""

def memoriser():
    params = []
    def inner(*args):
        params.append(', '.join(map(str, args)))
        return params
    return inner


add_to_list = memoriser()

# Передача параметров в функцию и далее в список параметров params
add_to_list(1, 2, 3)
add_to_list('abc')

# Извлечение сохранённых параметров
for params in add_to_list():
    print(params)

# 1, 2, 3
# abc
