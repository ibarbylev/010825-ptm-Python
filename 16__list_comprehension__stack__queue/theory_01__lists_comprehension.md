## Определение

**List comprehension** (LC) — это способ создания списка из итерируемого объекта в одной строке  
с помощью выражения, цикла и (опционально) условий.

Общий шаблон:

```python
[выражение for переменная in итерируемый_объект if условие]
```

⚠️ ⚠️ ⚠️ 
ВАЖНО: 
Если логика выражения сложнее базового шаблона, его КРАЙНЕ ЖЕЛАТЕЛЬНО разбить на блоки. 

---

## 1. Базовый LC

```python
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print(squares)  # [1, 4, 9, 16, 25]
```

---

## 2. LC с условием (`if` после цикла)

```python
nums = [1, 2, 3, 4, 5]
even = [x for x in nums if x % 2 == 0]
print(even)  # [2, 4]
```

---

## 3. LC с тернарным оператором (`if ... else ...`)

Тут `if` стоит **внутри выражения**, а не после цикла.

```python
nums = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in nums]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']
```

---

## 4. Вложенный LC (двойной `for`)

```python
pairs = [(x, y) for x in [1, 2, 3] for y in [10, 20, 30]]
print(pairs)
# [(1, 10), (1, 20), (1, 30), (2, 10), (2, 20), (2, 30), (3, 10), (3, 20), (3, 30)]
```

Аналогично:

```python
pairs = []
for y in [10, 20, 30]:
    for x in [1, 2, 3]:
        pairs += [(x, y)]
print(pairs)
# [(1, 10), (1, 20), (1, 30), (2, 10), (2, 20), (2, 30), (3, 10), (3, 20), (3, 30)]
```

---

## 5. Вложенные списки (LC внутри LC)

```python
matrix = [[x*y for x in range(1, 4)] for y in range(1, 4)]
print(matrix)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

Аналогично:

```python
matrix = []
for y in range(1, 4):
    
    sub_matrix = []
    for x in range(1, 4):
        sub_matrix += [x*y] 
        
    matrix += [sub_matrix]
    
print(matrix)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

---

## 6. LC с несколькими условиями

```python
nums = range(10)
filtered = [x for x in nums if x % 2 == 0 if x > 3]
print(filtered)  # [4, 6, 8]
```

Аналогично:

```python
nums = range(10)

filtered = []
for x in nums:
    if x % 2 == 0:
        if x > 3:
            filtered += [x]
print(filtered)  
# [4, 6, 8]
```
---

## 7. LC + функции

```python
words = ["hello", "world", "python"]
lengths = [len(w) for w in words]
print(lengths)  # [5, 5, 6]
```

---

## 8. LC для "развёртки" вложенных структур (flattening)

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

---

## 9. LC с `if...else` и дополнительным фильтром

```python
nums = [0, 1, 2, 3, 4, 5]
labels = ["zero" if x == 0 else "even" if x % 2 == 0 else "odd"
          for x in nums if x != 3]
print(labels)  # ['zero', 'odd', 'even', 'even', 'odd']
```

---

## 10. Генератор вместо списка (оптимизация памяти)

```python
gen = (x**2 for x in range(1000))  # tuple comprehension - это генератор!
print(next(gen))  # 0
print(next(gen))  # 1
```

---

# Алгоритм разбора сложного LC на блоки

Сформулируем правило "разбора" (превращения) LC в блоковую структуру:

1. Переменную LC (`result`) приравниваем пустому списку.

2. Временно отбрасываем `выражение` (то, что стоит слева от первого `for`).  
   (на всякий случай: тернарный оператор - это ТОЖЕ `выражение`)

3. Каждый следующий `for` или `if` (сохраняя порядок их следования!)
   * переносим на новую строку 
   * и превращаем в блоковый оператор.

4. Вставляем внутрь самого внутреннего блока: `result.append(выражение)`
---

### Пример:

List Comprehension:

```python
result = [f"{x}-{y}-{z}" for x in range(1, 4) for y in range(1, 4) if x * y % 2 == 0 for z in "abc" if z != 'b' if x + y < 5]
print(result)
```

Разворачивается как:

```python
result = []

for x in range(1, 4):
    for y in range(1, 4):
        if x * y % 2 == 0: 
            for z in "abc": 
                if z != 'b': 
                    if x + y < 5:
                        result.append(f"{x}-{y}-{z}")
print(result)
```

