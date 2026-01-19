 ## Конструкция `yield from`
 
### Простое (неполное) определение

`yield from` - это удобный способ получить генераторную функцию  
из любого итерируемого объекта.

И кстати, эта конструкция допустима ТОЛЬКО внутри тела генераторной функции.

```python
gen_express = (n for n in range(5))
nums_str = 'abcde'
nums_range = range(5)

def gen_f():
    for char in 'ABCDE':
        yield char


def outer_gen(iterable1, iterable2, iterable3, coll_1):
    yield from iterable1
    yield from iterable2
    yield from iterable3
    yield from coll_1()
    
    
# 0, 1, 2, 3, 4, a, b, c, d, e, 0, 1, 2, 3, 4, A, B, C, D, E, 


gen = outer_gen(gen_express, nums_str, nums_range, gen_f)

for x in gen:
    print(x, end=", ")
```

Как видим, для `yield from` годится вся, включая генераторную функцию.  
Правда, последнюю надо добавить с скобками, чтоб получить генератор.


### Полное определение

Конструкция `yield from` позволяет:
1. последовательно получать все элементы вложенного генератора/итерируемого.
2. автоматически передавать внутрь вложенного генератора:

   * отправленные через `.send()` значения,
   * исключения,
   * завершение итерации.

3. возвращать значение из `return` внутреннего генератора (если оно есть).