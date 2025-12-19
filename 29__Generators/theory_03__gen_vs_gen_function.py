from typing import Generator, Iterator, Callable

def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)

print('--- Где будет True, и где будет False? ---')

print(isinstance(countdown, Iterator))
print(isinstance(countdown, Generator))
print(isinstance(countdown, Callable))

print('------------------------------------------')

print(isinstance(gen, Iterator))
print(isinstance(gen, Generator))
print(isinstance(gen, Callable))

print('=========== Запуск генератора ============')

for n in gen:
    print(n)

