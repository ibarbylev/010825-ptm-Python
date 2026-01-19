"""
Фамилия     Имя         Часов   Ставка
Лютиков     Руслан      60      1000
Иванов      Иван        45      400
Докукин     Филимон     20      1000
Ромашкин    Сидор       45      500
"""

from collections import namedtuple

Salary = namedtuple('Salary', ('surname', 'name', 'worked', 'rate'))


def get_salary(line):
    '''
    Вычисление зарплаты работника
    '''

    result = ()

    line = line.split()
    if line:
        data = Salary(*line)
        fio = ' '.join((data.surname, data.name))
        salary = int(data.worked) * int(data.rate)
        result = (fio, salary)

    return result


def test_get_salary_sum():
    assert get_salary('Лютиков   Руслан     60    1000') ==\
                     ('Лютиков Руслан', 60000), 'Неверная сумма коррект'


def test_get_incorrect_salary_sum():
    assert get_salary('Лютиков   Руслан     60    1000') !=\
                     ('Лютиков Руслан', 70000), 'Неверная сумма инкоррект'


def test_get_salary_fio():
    assert get_salary('Лютиков   Руслан     60    1000')[0] ==\
                     'Лютиков Руслан', 'Неверное имя'


def test_get_salary_empty():
    assert get_salary('') == (), 'Непустые данные'


def test_get_salary_wrong_format():
    assert get_salary(' ') == (), 'Непустые данные'


if __name__ == "__main__":
    test_get_salary_sum()
    test_get_incorrect_salary_sum()
    test_get_salary_fio()
    test_get_salary_empty()
    test_get_salary_wrong_format()

    print(get_salary(''))
