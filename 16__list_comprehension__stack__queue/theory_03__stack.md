## Определение

**Стек (stack)** — это структура данных типа **LIFO** 
(*Last In, First Out* — «последним пришёл, первым ушёл»).



## Простейшая реализация на списке

```python
stack = []  # создаём пустой стек

# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# pop
top = stack.pop()
print("Сняли:", top)      # 3
print("Стек:", stack)     # [1, 2]

# peek (смотрим верхний элемент)
print("Верхний:", stack[-1])  # 2
```


---

## Пример использования (проверка скобок)

```python
def check_parentheses(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)  # push
        elif char == ")":
            if not stack:
                return False
            stack.pop()         # pop
    return not stack

print(check_parentheses("(())"))   # True
print(check_parentheses("(()"))    # False
print(check_parentheses("())("))   # False
```

