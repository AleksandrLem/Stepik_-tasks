# Напишите программу, записывающую в текстовый файл random.txt
# 25 случайных чисел в диапазоне от
# 111 до
# 777 (включительно), каждое с новой строки.

import random

# создаем список с 25 случайными числами
lst_num = []
for _ in range(25):
    nums = str(random.randint(111, 777))+'\n'
    lst_num.append(nums)
# или генератор списка:
# lst_num = [f'{random.randint(111, 777)}\n' for _ in range(25)]

# записываем числа из списка в файл random.txt
with open('random.txt', 'w', encoding='utf-8') as file:
    file.writelines(lst_num)

# короткое решение
with open('random.txt', 'w', encoding='utf-8') as file:
    file.writelines([f'{random.randint(111, 777)}\n' for _ in range(25)])
