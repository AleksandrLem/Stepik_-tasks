# Напишите программу, которая выводит на экран случайную строку из файла.

import random

file = open('text.txt', 'r', encoding='utf-8')

lst_txt = file.readlines()
# первое решение
rand = random.randint(0, len(lst_txt)-1)
print(lst_txt[rand])
# второе решение
print(random.choice(lst_txt))

file.close()
