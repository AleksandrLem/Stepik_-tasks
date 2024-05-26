# Вам доступны два текстовых файла first_names.txt и last_names.txt,
# один с именами, другой с фамилиями.

# Напишите программу, которая c помощью модуля random создает
# 3 случайные пары имя + фамилия, а затем выводит их, каждую
# на отдельной строке.

import random

with open('Stepik_tasks/first_names.txt', 'r', encoding='utf-8') as f_name, open('Stepik_tasks/last_names.txt', 'r', encoding='utf-8') as l_name:
    # сначала читаем файлы с именами и фамилиями
    lst_f = f_name.read().split()
    lst_l = l_name.read().split()
    # рандомно выбираем три имени и три фамилии
    lst_f = random.sample(lst_f, 3)
    lst_l = random.sample(lst_l, 3)
    # проходим циклом по двум спискам, выводим имя и фамилию
    for f, l in zip(lst_f, lst_l):
        print(f, l)