### 4. ISP: Interface Segregation Principle (принцип разделения интерфейсов) 

***Клиенты не должны зависеть от интерфейсов, которые они не используют.***

Иными словами, лучше создавать несколько узкоспециализированных ("тонких") интерфейсов,  
чем один «толстый», который вынуждает классы реализовывать лишние методы.

Такой подход уменьшает лишние зависимости, делает код более гибким и проще поддерживается.

---

### Пример нарушения принципа ISP:

```python
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

# Класс Robot вынужден реализовать метод eat(), хотя роботы не едят
class Robot(Worker):
    def work(self):
        print("Robot is working")
    
    def eat(self):
        raise NotImplementedError("Robots do not eat")
```

Проблема: 
* `Robot` вынужден реализовать метод `eat()`, который ему не нужен. 
* Любой код, полагающийся на `Worker`, может вызвать `eat()` и получить ошибку.

---

**Применение ISP через разделение интерфейсов:**

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

class Robot(Workable):
    def work(self):
        print("Robot is working")
```

Теперь:

* `Human` реализует оба интерфейса — работает и ест.
* `Robot` реализует только интерфейс `Workable`.
* Код, который использует `Workable`, может работать с любым «работником», не заботясь о методе `eat()`.

