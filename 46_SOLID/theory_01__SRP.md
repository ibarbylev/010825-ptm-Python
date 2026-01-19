### 1. SPR: Single Responsibility Principle (принцип единственной ответственности)

***Каждый класс должен иметь только одну причину для изменения.***   

В переводе на человеческий: 
* Каждый класс должен решать только **одну конкретную задачу**. 
* Решать несколько вещей сразу — значит усложнять и поддержку, и тестирование.

Как видим, всё предельно просто и ясно.  
Дело "за малым": решить, что в Вашем проекте считается ***одной конкретной задачей***?

---

### Пример нарушения SRP:

```python
class UserManager:
    def __init__(self, username):
        self.username = username
    
    def save_user(self):
        # сохраняем пользователя в базу данных
        print(f"Saving {self.username} to database")
    
    def print_user(self):
        # выводим информацию о пользователе
        print(f"User: {self.username}")
```

Здесь `UserManager` сразу делает две вещи:

1. Работа с данными (сохраняет пользователя).
2. Отображение информации (печатает данные).

Если вы захотите изменить способ вывода на экран, придётся трогать класс, который отвечает за данные — нарушение SRP.

---

**Применение SRP:**

```python
class User:
    def __init__(self, username):
        self.username = username

# Миксин для сохранения пользователя
class SaveMixin:
    def save(self):
        print(f"Saving {self.username} to database")

# Миксин для вывода пользователя
class PrintMixin:
    def print_user(self):
        print(f"User: {self.username}")

# Класс, который комбинирует User с функционалом миксинов
class UserWithFeatures(User, SaveMixin, PrintMixin):
    pass

# Использование
user = UserWithFeatures("Alice")
user.save()        # Saving Alice to database
user.print_user()  # User: Alice

```

Теперь задачи разделены:

* `User` — просто хранит данные.
* `SaveMixin` — отвечает только за сохранение пользователя.
* `PrintMixin` — отвечает только за отображение информации.

Такой код проще поддерживать, расширять и тестировать.
