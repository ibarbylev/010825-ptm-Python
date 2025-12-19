"""
Поэтому, крайне удобно иметь объект, который:
- не только содержит все присущие ему значения и функции
- но и может "подставить" свои значения в свои функции без лишних "телодвижений".

И этот объект - экземпляр класса (class instance).
"""


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


square = Square(3)
print(square.side)        # 3
print(square.area())      # 9
print(square.perimeter()) # 12

"""
Объект square - квадрат со стороной 3 условных единицы.
Его площадь и его периметр рассчитываются автоматически, поскольку
"подставлять" значения в них НЕ НАДО!
"""