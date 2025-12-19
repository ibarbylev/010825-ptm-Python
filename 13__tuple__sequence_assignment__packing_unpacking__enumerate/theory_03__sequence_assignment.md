## Присваивание последовательности (sequence assignment)


**Sequence assignment** — это присваивание элементов последовательности (списка, тюпла, строка)  
нескольким переменным одновременно.

Количество переменных должно СТРОГО совпадать с количеством элементов последовательности, иначе будет ошибка.


```python
a, b, c = 'ABC'
print('a:', a)  # A
print('b:', b)  # B
print('c:', c)  # C


a, b = 'ABC'
# ValueError: too many values to unpack (expected 2)


a, b, c, d = 'ABC'
# ValueError: not enough values to unpack (expected 4, got 3)
```

## Можно ли избежать ошибки в последних двух случаях?

ОТВЕТ: Да, если использовать packing.

```python

a, b, *rest = 'ABC'
print('a:', a)          # A
print('b:', b)          # B
print('rest:', rest)    # [C]


a, b, c, *rest = 'ABC'
print('a:', a)          # A
print('b:', b)          # B
print('c:', c)          # C
print('rest:', rest)    # []
```