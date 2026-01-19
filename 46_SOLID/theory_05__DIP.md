### 5. DIP: Dependency Inversion Principle (принцип инверсии зависимостей)

***Модули верхнего уровня не должны зависеть от модулей нижнего уровня.  
Оба типа должны зависеть от абстракций (интерфейсов или базовых классов).  
Абстракции не должны зависеть от деталей, а детали должны зависеть от абстракций.***

Это делает систему гибкой: можно легко менять конкретные реализации без изменения кода, который их использует.

---

### **Пример на Python**

**Нарушение DIP:**

```python
class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # зависимость от конкретной реализации

    def save_user(self, user):
        self.db.save(user)
```

Проблема: `UserService` жестко зависит от `MySQLDatabase`. Если захотим сменить базу на PostgreSQL, придётся менять сам класс `UserService`.

---

**Применение DIP через абстракции:**

```python
from abc import ABC, abstractmethod

# Абстракция
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

# Конкретные реализации
class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to PostgreSQL database")

# Класс верхнего уровня зависит от абстракции
class UserService:
    def __init__(self, db: Database):
        self.db = db

    def save_user(self, user):
        self.db.save(user)

        
mysql_service = UserService(MySQLDatabase())
mysql_service.save_user("Alice")  # Saving Alice to MySQL database

postgres_service = UserService(PostgreSQLDatabase())
postgres_service.save_user("Bob")  # Saving Bob to PostgreSQL database
```

* Теперь `UserService` **не зависит от конкретной базы**, а только от интерфейса `Database`. 
* Любую реализацию можно подставлять без изменения логики верхнего уровня — это и есть DIP.


