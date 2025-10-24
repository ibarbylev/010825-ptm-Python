
## Операторы расширенного присваивания (augmented assignment operators)

| Оператор | Пример с приращением          | Результат |
|----------|-------------------------------|-----------|
| `+`      | `x = 5; x += 3`               | `8`       |
| `-`      | `x = 5; x -= 2`               | `3`       |
| `*`      | `x = 5; x *= 4`               | `20`      |
| `/`      | `x = 5; x /= 2`               | `2.5`     |
| `//`     | `x = 5; x //= 2`              | `2`       |
| `%`      | `x = 5; x %= 2`               | `1`       |
| `**`     | `x = 2; x **= 3`              | `8`       |


Как правило, по расширенному присваиванию можно определить,  
является ли тип данных изменяемым (`mutable`) или неизменяемым (`immutable`).

```python
x = 5
address_1 = id(x)
x += 1
address_2 = id(x)

print("Is x mutable?", address_1 == address_2)
# Is x mutable? False

lst = [5]
address_1 = id(lst)
lst += [1]
address_2 = id(lst)

print("Is lst mutable?", address_1 == address_2)
# Is lst mutable? True
```