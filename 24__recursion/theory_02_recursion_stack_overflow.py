"""Пример переполнения стека"""


def countdown_recursion(n):
    if n > 0:
        print(n)
        return countdown_recursion(n - 1)
    else:
        print("Done!")


countdown_recursion(10000)
