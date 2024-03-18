# На вход программе подается строка текста. Напишите программу,
# которая выводит слово, которое встречается реже всего, без учета регистра.
# Если таких слов несколько, выведите то, которое меньше в
# лексикографическом порядке.


import re, pprint

text = '''London is the capital of Great Britain.
More than six million people live in London.
London lies on both banks of the river Thames.
It is the largest city in Europe and one of the
largest cities in the world. London is not only the
capital of the country, it is also a very big port,
one of the greatest commercial centres in the world,
a university city, and the seat of the government of Great Britain!'''

# удаляем все знаки препинания в тексте, все слова переводим в
# нижний регистр, создаем список всех слов
new_text = re.sub(r'[^\w\s]','', text).lower().split()
print(new_text)

# создаем словарь
result = {}

# заполняем словарь, где ключ - слово, значение - количество раз,
# которое это слово встречается в тексте
for el in new_text:
    result[el] = result.get(el, 0) + 1

pprint.pprint(result)

# находим самое редковстречающееся слово в словаре
for key in sorted(result):
    if result[key]==min(result.values()):
        print(key)
        break