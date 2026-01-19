## Строки - неизменяемый (`immutable`) тип данных.  

Доказательства находится [здесь](../03__arithmetic_operations__type_conversion/theory_03__augmented_assignment_operators.md)

**Важно:**  
Из этого вовсе не следует, что нельзя проводить операции по изменению строк!  
Просто результат этого изменения будет находиться в новой (другой) ячейке памяти:

```python
s = 'Hello'
print(id(s))  # 139908104970544
print(s)      # Hello
s += ' world!'
print(id(s))  # 139907897652336
print(s)      # Hello world!
```

## Различные кодировки строк

Строка - это упорядоченный набор символов.  
Каждый символ имеет свой код.  
В Python 2 использовалась [кодировка `ascii`](https://en.wikipedia.org/wiki/ASCII#Printable_character_table)

Именно для перевода строк в другую кодировку, а именно в [кодировку `Unicode`](https://en.wikipedia.org/wiki/UTF-8#Description),    
перешли на Python 3.