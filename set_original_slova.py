import re

s = '.d ,d ;d :d -d ?d !d'

# удаляем из строки знаки препинания, все буквы приводим к нижнему регистру, создаем список слов
s = re.sub(r'[.,;:?!-]', '', s).lower().split()
print(s)
print(set(s))
print(len(set(s)))
