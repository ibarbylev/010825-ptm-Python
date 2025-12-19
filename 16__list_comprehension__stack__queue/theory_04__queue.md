## Определение

**Очередь (queue)** — это структура данных типа **FIFO**  
(*First In, First Out* — «первым пришёл, первым ушёл»).

Пример из жизни: очередь в магазине — первый вошёл, первый обслужен.


---

## 1. Реализация на `list`

```python
queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # [1, 2, 3]

# dequeue (удаляем из начала!)
first = queue.pop(0)
print("Обслужили:", first)  # 1
print("Очередь:", queue)    # [2, 3]

# peek
print("Первый:", queue[0])  # 2
```

⚠️ Минус: `pop(0)` медленный (O(n)), потому что все элементы сдвигаются.

---

## 2. Реализация на `collections.deque` (рекомендуется)

```python
from collections import deque

queue = deque()

# enqueue
queue.append("a")
queue.append("b")
queue.append("c")
print(queue)  # deque(['a', 'b', 'c'])

# dequeue
print(queue.popleft())  # a
print(queue.popleft())  # b
print(queue)            # deque(['c'])

# peek
print(queue[0])         # c
```

Здесь `popleft()` работает за O(1), поэтому `deque` → идеален для очередей.

