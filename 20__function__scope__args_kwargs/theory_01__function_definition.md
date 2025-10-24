## Функция в Python.

### Определение 

**Функция** — это именованный блок кода, который 
- выполняет определённое действие 
- и может быть вызван в программе многократно.

Функции позволяют 
- избегать дублирования кода (лаконичность и читабельность)
- структурировать код, разбить его на независимые модули, которые 
  - удобно по одному отладить по одному
  - и затем объединить в единое целое ("разделяй и властвуй")


### Синтаксис

```python
# Определение функции

def function_name(parameters):
    """docstring описание функции""" # (optional)
    ...
    # function_body
    ...
    expression = ...
    return expression  # (optional)
    
    
# Вызов функции
arguments = ...
function_name(arguments)
```


* `def` — ключевое слово, используется для определения функции 
* `function_name` — имя функции (`snake_case`, обычно глагол как действие)
* `parameters` — (optional) значения, которые функция может принимать при вызове
* `"""docstring"""` — (optional) краткое описание того, что функция делает
* `function_body` — тело функции (исполняемый функцией код)
* `return` — (optional) оператор как часть тела функции. Возвращает значение в точку вызова функции
* ВАЖНО: функция, которая ничего не возвращает, всё равно возвращает `None`


```python
def greet(name):
    """Prints a greeting with the given name."""
    print(f"Hello, {name}!")

greet("John")
# Hello, John!
```


Если функция должна **вернуть результат**, используется ключевое слово **`return`**:

```python
def add(a, b):
    return a + b


result = add(3, 5)
print(result)  # 8
```

Если `return` не указан, функция возвращает `None`.

### Использование нескольких операторов `return` в одной функции

В ряде случаев это ОЧЕНЬ удобно:

```python
def is_zero_or_positive(num):
    if isinstance(num, (int, float)) and num >= 0:
        return True
    return False

print(is_zero_or_positive("asdf"))  # False
print(is_zero_or_positive(5))       # True
print(is_zero_or_positive(-5))      # False

```

В данном примере экономим `else` и делаем код более читабельным.


### Может ли `return` вернуть БОЛЕЕ ОДНОГО результат


Нет.

Но мы всегда можем объединить несколько результатов в коллекцию.

```python
def get_all_even_numbers(*args):
    return [n for n in args if n % 2 == 0]


print(get_all_even_numbers(1, 2, 3, 4, 5, 6, 7))
# [2, 4, 6]
```
