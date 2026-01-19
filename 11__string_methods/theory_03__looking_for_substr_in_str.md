# Методы поиска подстроки в строке

| Метод                               | Что делает                                     | Возвращает при успехе | При неудаче  | Пример                             |
|-------------------------------------| ---------------------------------------------- | --------------------- | ------------ | ---------------------------------- |
| `find(sub[, start[, end]])`         | Индекс первого вхождения подстроки             | `int` (позиция)       | `-1`         | `"hello world".find("world")  # 6` |
| `rfind(sub[, start[, end]])`        | Индекс последнего вхождения подстроки          | `int` (позиция)       | `-1`         | `"test test".rfind("test")  # 5`   |
| `index(sub[, start[, end]])`        | Как `find`, но с исключением                   | `int` (позиция)       | `ValueError` | `"hello".index("he")  # 0`         |
| `rindex(sub[, start[, end]])`       | Как `rfind`, но с исключением                  | `int` (позиция)       | `ValueError` | `"banana".rindex("na")  # 4`       |
| `startswith(prefix[, start[, end]])` | Проверяет, начинается ли строка с подстроки    | `True` / `False`      | `False`      | `"Python".startswith("Py")  # True` |
| `endswith(suffix[, start[, end]])`  | Проверяет, оканчивается ли строка на подстроку | `True` / `False`      | `False`      | `"Python".endswith("on")  # True`  |
| `count(sub[, start[, end]])`        | Считает количество вхождений подстроки | `int` (число вхождений) | 0 | `"banana".count("na") # 2` |
---

### Итоговое заключение

* Для **поиска позиции подстроки**:

  * `find` и `rfind` безопаснее (возвращают `-1`, если не нашли).
  * `index` и `rindex` строже (вызывают `ValueError`, если не нашли).
  
Поэтому `index` и `rindex` обычно используют вместе с проверкой

```python
text = 'substring substring'
if 'sub' in text:
    print(text.index('sub'))   # 0
    print(text.rindex('sub'))  # 13
else:
    print('Нет совпадений')
```


