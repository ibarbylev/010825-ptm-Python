### 2. OCP: Open/Closed Principle (принцип открытости/закрытости)

***Сущности (классы, функции, модули) должны быть*** 
* ***открыты для расширения,***
* ***но закрыты для изменения.*** 

Это значит, что 
* для добавления нового поведения не нужно менять уже существующий, проверенный код — 
* вместо этого мы расширяем его через наследование или композицию.

Такой подход 
* снижает риск ошибок при доработках 
* и делает систему более устойчивой.

---

### **Пример на Python**

**Нарушение OCP:**

```python
class DiscountCalculator:
    def calculate(self, price, customer_type):
        if customer_type == "regular":
            return price * 0.9  # 10% скидка
        elif customer_type == "vip":
            return price * 0.8  # 20% скидка

# Если добавляется новый тип клиента, приходится вносить изменения в сам класс 
# => есть риск повредить проверенный и отлаженный код
```

Проблема: каждый раз при добавлении нового типа клиента мы **меняем существующий класс**, что нарушает OCP.

---

**Применение OCP через расширение:**

```python
# Базовый класс (абстракция)
class DiscountStrategy:
    def apply_discount(self, price):
        return price

# Конкретные стратегии
class RegularDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.8

# Класс, который использует стратегию
class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, price):
        return self.strategy.apply_discount(price)

    
# Использование:
regular = DiscountCalculator(RegularDiscount())
vip = DiscountCalculator(VIPDiscount())

print(regular.calculate(100))  # 90.0
print(vip.calculate(100))      # 80.0
```

Теперь, если нужно добавить новый тип скидки, например **"employee"**, мы 
* создаём новый класс `EmployeeDiscount` 
* и при этом НЕ изменяем `DiscountCalculator`. 

Это полностью соблюдает **OCP**.

