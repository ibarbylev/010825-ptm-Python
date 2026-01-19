## Области видимости в Python (LEGB)

Python использует правило **LEGB**, которое определяет порядок поиска переменной:

1. **L — Local**
   Локальная область внутри функции или лямбда-выражения.

2. **E — Enclosing**
   Область всех внешних функций (для вложенных функций).

3. **G — Global**
   Область модуля (файл Python).

4. **B — Built-in**
   Встроенные имена Python (например, `len`, `print`, `range`).

---

### Простой пример LEGB

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print('x from local:', x)

    inner()
    
    print('x from outer:', x)

outer()

print('x from global:', x)

print('len(x) =', len(x))
```

Вывод:

```
x from local: local
x from outer: enclosing
x from global: global
len(x) = 6

```

### Вывод:

Python ищет `x` в порядке: **Local → Enclosing → Global → Built-in**.

