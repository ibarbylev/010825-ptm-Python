def double(x):
    return x * 2


if __name__ == "__main__":
    assert double(2) == 4, f"Ошибка в double(2): должно быть 4, получено {double(2)}"