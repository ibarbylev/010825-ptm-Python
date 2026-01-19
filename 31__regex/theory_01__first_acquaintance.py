"""
1. Язык регулярных выражений - это самостоятельный макроязык.
    Как, например, SQL.
    (впрочем, некоторые считают его всего лишь "формальным языком шаблонов")

2. Этот макроязык используется в большинстве языков высокого уровня.
    (в той или иной степени).


Зачем он вообще нужен?

1. Чтобы очень легко и удобно "вытащить" из текста ровно то, что нам нужно.
2. Чтобы проверить, действительно ли в тексте есть то, что нам нужно.
3. Чтобы быстро и удобно заменить в тексте ненужное на нужное.
4. Чтобы легко и удобно разбить текст по сложным правилам.


С основными элементами макроязыка регулярных выражений (regex) можно ознакомиться здесь:
https://it4each.com/blog/reguliarnye-vyrazheniia-predislovie/



Ниже пример простейшего поиска кол-ва повторений паттерна в тексте.
Это делается на чистом Python без всякого regex.
Поскольку задача очень простая.

Но если вместо pattern использовать регулярное выражение,
то можно получить ГОРАЗДО более интересные результаты.
"""

from lorem_text import lorem

# print(lorem.paragraph())

text = """Consequatur est quos repellat obcaecati, corporis corrupti cupiditate qui 
tempore nesciunt possimus dolores animi voluptates culpa suscipit, eum excepturi 
laboriosam nemo commodi ullam? Odit placeat nemo sint voluptatum in illum accusamus 
saepe asperiores, distinctio odio harum? Dignissimos necessitatibus quaerat modi, 
magni ex debitis voluptas, neque error totam odit, molestias odio voluptatem obcaecati 
minus vel nostrum repudiandae iure, blanditiis corporis corrupti ducimus aperiam.
"""

patten = r'mo'

print(text.count(patten))  # 6
