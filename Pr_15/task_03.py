""" 03 Извлечение email-адресов

Реализуйте программу, которая:
- находит в тексте все email-адреса, соответствующие следующим критериям:
    - перед @ допускаются буквы, цифры, точки (.) и подчёркивания (_),
            но не начинается и не заканчивается точкой.
    - после @ следует:
        - домен второго уровня: буквы, цифры, дефисы, точки.
        - затем домен верхнего уровня (например, .com, .org, .net, .pl), от 2 до 3 букв.
    - email не может содержать пробелы.

Данные:
text = '''
Valid:
- support@mail.com
- info@company.org
- personal_email123@edu.university.net
- user.name@sub.domain.com
- contact_us123@my-site.org
- hello.world@some.place.travel
- admin@server.local
- support@company-name.de
- user@data.edu.pl

Invalid:
- .support@mail.com
- support.@mail.com
- user@domain,com
- name@domaincom
- name@domain.c
- user@domain.toolongtldddddd
- no@space .com
- bad@@mail.com
- missing@dotcom
'''

Пример вывода:
support@mail.com
info@company.org
personal_email123@edu.university.net
user.name@sub.domain.com
contact_us123@my-site.org
support@company-name.de
user@data.edu.pl

"""
import re

text = """
Valid:
- support@mail.com
- info@company.org
- personal_email123@edu.university.net
- user.name@sub.domain.com
- contact_us123@my-site.org
- support@company-name.de
- user@data.edu.pl

Invalid:
- .support@mail.com
- support.@mail.com
- user@domain,com
- name@domaincom
- name@domain.c
- user@domain.toolongtldddddd
- hello.world@some.place.travel
- no@space .com
- bad@@mail.com
- missing@dotcom
"""

pass



# support@mail.com
# info@company.org
# personal_email123@edu.university.net
# user.name@sub.domain.com
# contact_us123@my-site.org
# support@company-name.de
# user@data.edu.pl
# support@mail.com