### ПОДКЮЧЕНИЕ

```python
from pymongo import MongoClient
from local_settings import MONGODB_URL_WRITE

with MongoClient(MONGODB_URL_WRITE) as client:
    db = client.get_database('DB_name')
    collection = db.get_collection('collection_name')

    # Получить все документы коллекции
    docs = collection.find()
```



### ПОИСК (READ)

### Найти все документы, удовлетворяющие условию

```python
collection.find({"price": 100})
```

### Найти один документ

```python
collection.find_one({"name": "Laptop"})
```

### Сортировка

```python
collection.find().sort("price", 1)   # по возрастанию
collection.find().sort("price", -1)  # по убыванию
```

### Ограничение и пропуск

```python
collection.find().limit(5)
collection.find().skip(10)
```

---

### ВСТАВКА (CREATE)

### Вставка одного документа

```python
collection.insert_one({
    "name": "Pen",
    "price": 1.5,
    "stock": 100
})
```

### Вставка нескольких документов

```python
collection.insert_many([
    {"name": "Notebook", "price": 4, "stock": 50},
    {"name": "Backpack", "price": 30, "stock": 10}
])
```

---

### ОБНОВЛЕНИЕ (UPDATE)

### Обновить один документ

```python
collection.update_one(
    {"name": "Pen"},
    {"$set": {"price": 1.8}}
)
```

### Обновить несколько документов

```python
collection.update_many(
    {"stock": {"$gt": 0}},
    {"$set": {"available": True}}
)
```

### Увеличить числовое поле

```python
collection.update_many(
    {},
    {"$inc": {"stock": 5}}
)
```

### Умножить значение

```python
collection.update_many(
    {},
    {"$mul": {"price": 1.2}}
)
```

### Удалить поле

```python
collection.update_one(
    {"name": "Pen"},
    {"$unset": {"available": ""}}
)
```

---

### УДАЛЕНИЕ (DELETE)

### Удалить один документ

```python
collection.delete_one({"name": "Pen"})
```

### Удалить несколько документов

```python
collection.delete_many({"stock": 0})
```

### Очистить коллекцию полностью

```python
collection.delete_many({})
```

---

### Итого (CRUD)

| Операция | Метод                       |
| -------- | --------------------------- |
| Create   | `insert_one`, `insert_many` |
| Read     | `find`, `find_one`          |
| Update   | `update_one`, `update_many` |
| Delete   | `delete_one`, `delete_many` |

