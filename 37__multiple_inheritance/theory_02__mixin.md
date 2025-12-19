### Понятие Mixin

Это класс, который 
* передаёт наследникам свою функциональность,
* но не способен создавать свои собственные объекты.

***"Воспитывать чужих детей может, а иметь своих собственных — нет."***

Главная идея:

* Mixin добавляет **одну или несколько функций** к классу.
* Обычно **не хранит состояние** (атрибуты объекта), а лишь предоставляет методы.
* Используется вместе с **множественным наследованием**.

---

#### Пример

Создание текстового редактора.  
Условие: для разных клиентов нужен разный набор функционала

```python
# Основной класс
class Document:
    def __init__(self, name, content):
        self.name = name
        self.content = content


class EditDocument(Document):
    def edit(self):
        self.content += "\nТекст был отредактирован"
        return self


# ===== Возможные варианты дополнительного функционала =====
# Mixin для отправки документа по email
class EmailMixin:
    def send_email(self, recipient):
        print(f"Sending document '{self.name}' to {recipient} via email...")


# Mixin для сохранения документа на диск
class SaveMixin:
    def save(self):
        print(f"Saving document '{self.name}' to disk...")


# Mixin для печати документа
class PrintMixin:
    def print_doc(self):
        print('-' * 50,)
        print(f"Printing document '{self.name}' \n{self.content}")
        print('-' * 50, '\n')


# ======= Создаём полноценный текстовой редактор =========

class TextEditor(EditDocument, EmailMixin, SaveMixin, PrintMixin):
    """Текстовый редактор с возможностью редактирования, сохранения, печати и отправки по email"""
    pass


doc = TextEditor("MyDoc", "This is the original content.")

# Печатаем до изменений
doc.print_doc()

# Редактируем документ
doc.edit()

# Сохраняем
doc.save()

# Отправляем по email
doc.send_email("person@example.com")

# Печатаем
doc.print_doc()
```

**Резюме**
Добавляя разный набор миксинов в дочерний класс мы можем легко моделировать нужной набор функционала.  
Без всякого вмешательства в исходный (отлаженный!) код.

---

### Преимущества такого подхода

1. **Повторное использование кода:**

   * Каждый Mixin можно подключать к любому другому классу, например, к `SpreadsheetEditor` или `PresentationEditor`.

2. **Разделение ответственности:**

   * Логика отправки, сохранения и печати **отделена от основного класса документа**.

3. **Гибкость:**

   * Если нужен редактор без печати, просто не наследуем `PrintMixin`.

