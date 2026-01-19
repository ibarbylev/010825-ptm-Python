from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper's doc_string"""
        print(50 * '*')
        f = func(*args, **kwargs)
        print(50 * '*')
        return f
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper's doc_string"""
        print(50 * '=')
        f = func(*args, **kwargs)
        print(50 * '=')
        return f
    return wrapper


@decorator1
@decorator2
def some_func():
    print('printing some_func _')


"""
Как видим, изначально функцию some_func() декорируют оба декоратора.
Но есть метод, который позволяет отменить действие декораторов.
"""

print("------------------ Работают оба декоратора ------------------")
some_func()


print("\n\n------------------ Снять оба декоратора ------------------")
some_func.__wrapped__.__wrapped__()


print("\n\n------------------ Снять оба декоратора и добавить первый ------------------")
@decorator1
def f1():
    return some_func.__wrapped__.__wrapped__()


f1()


print("\n\n------------------ Снять только один внешний декоратор (@decorator1) ------------------")

def f2():
    return some_func.__wrapped__()


f2()