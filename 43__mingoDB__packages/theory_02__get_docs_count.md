## ПОЛУЧЕНИЕ КОЛИЧЕСТВА ДОКУМЕНТОВ В `pymongo`

### При поиске

#### Рекомендуемый способ (без курсора)

```python
count = collection.count_documents({"price": {"$gt": 100}})
print(count)
```

✔️ Самый правильный и быстрый способ
❌ Не требует извлечения документов

---

#### ⚠️ Подсчёт через курсор (не рекомендуется для больших данных)

```python
cursor = collection.find({"price": {"$gt": 100}})
count = len(list(cursor))
print(count)
```

❌ Загружает все документы в память
✔️ Иногда допустим для учебных задач

---

#### Подсчёт при итерации курсора

```python
cursor = collection.find({})
count = 0

for _ in cursor:
    count += 1

print(count)
```

✔️ Работает всегда
❌ Медленно


---

### При добавлении документов в коллекцию

#### `inserted_id`

```python
result = collection.insert_one({"name": "Pen", "price": 2, "stock": 10})
print(1 if result.inserted_id else 0)
```


```python
result = collection.insert_many(documents)
print(len(result.inserted_ids))
```


---

### При обновлении документов коллекции

#### `matched_count` и `matched_count`

`update_one` / `update_many`

```python
result = collection.update_many(
    {"stock": {"$gt": 0}},
    {"$inc": {"stock": 1}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)
```

| Поле             | Значение                   |
| ---------------- | -------------------------- |
| `matched_count`  | сколько документов найдено |
| `modified_count` | сколько реально изменено   |

Документ может быть найден, но не изменён
(например, если значение уже такое же)

---


### После удаления 

#### `deleted_count`


`delete_one` / `delete_many`

```python
result = collection.delete_many({"stock": 0})
print(result.deleted_count)
```

---

### СВОДНАЯ ТАБЛИЦА

| Операция      | Как получить количество           |
| ------------- | --------------------------------- |
| find          | `count_documents(filter)`         |
| find (курсор) | `len(list(cursor))` ⚠️            |
| insert_one    | `inserted_id`                     |
| insert_many   | `len(inserted_ids)`               |
| update_*      | `matched_count`, `modified_count` |
| delete_*      | `deleted_count`                   |

