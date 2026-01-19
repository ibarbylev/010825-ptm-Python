"""
Module with function multiply_by_2 and its tests
"""


def multiply_by_2(num: int) -> int | str:
    """
    Function returns integer <num> multiplied by 2.
    """

    if isinstance(num, int):
        return 2 * num
    return 'Error!!! Argument <num> must be integer!!!'


d
print(multiply_by_2(5))


if __name__ == "__main__":
    assert multiply_by_2(2) == 4, 'Correct multiply positive is not true!'

    assert multiply_by_2(-2) == -4, 'Correct multiply negative is not true!'

    assert multiply_by_2(2) != 5, 'Incorrect multiply positive is not true!'

    assert multiply_by_2(-2) != -5, 'Incorrect multiply negative is not true!'

    assert multiply_by_2(0) == 0, 'Multiply by zero is not equal zero!'

    assert multiply_by_2("str") == 'Error!!! Argument <num> must be integer!!!', \
        'Wrong answer if <num> is string!'

    assert multiply_by_2(0.1) == 'Error!!! Argument <num> must be integer!!!', \
        'Wrong answer if <num> is float!'



