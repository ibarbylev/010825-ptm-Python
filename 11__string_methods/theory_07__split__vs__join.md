# Методы разделения и "сбора" строки

 
## 1 Метод `split()`

Синтаксис: `split(sep=None, maxsplit=-1)`  

Разбивает строку на список подстрок по указанному разделителю `sep`.  
Если `sep` не указан, - "разбивает" по пробельным символам.   
Допустимо ограничить число разбиений, указав `maxsplit`> 0


### Примеры

```python
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  
# ['apple', 'banana', 'cherry']

text2 = "one two   three"
words = text2.split()
print(words)  
# ['one', 'two', 'three']

text3 = "a,b,c,d,e"
print(text3.split(",", 2))  
# ['a', 'b', 'c,d,e']  (максимум 2 разбиения)
```

### 2. Метод `join()`

Синтаксис: `join(iterable)`

Объединяет элементы итерируемого объекта в одну строку вокруг "объединителя",  
указанного как аргумент метода `join()`. 

```python
words = ['apple', 'banana', 'cherry']
text = ", ".join(words)
print(text)  
# "apple, banana, cherry"

text = 'Python'
letters = list(text)  # ['P', 'y', 't', 'h', 'o', 'n']
print("".join(letters))  
# 'Python'
```


## Резюме

* `split()` — как ножницы, режет строку по указанному разделителю, превращая её в список строк.
* `join()` — как клей, склеивает список строк в одну строку, вокруг "объединителя".

