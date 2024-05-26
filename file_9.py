# Вам доступен текстовый файл text_country.txt с названиями стран и
# численностью их населения, разделенными символом табуляции '\t'.

# Напишите программу выводящую все страны, название которых
# начинается с буквы 'G', численность населения которых больше чем
# 500 000 человек, не меняя их порядок.


with open('text_country.txt', 'r', encoding='utf-8') as file:
    lst_file = [line.split() for line in file]
    # print(lst_file)
    for el in lst_file:
        if el[0][0] == 'G' and int(el[-1]) > 500_000:
            print(el[0])

# можно решить так:
# with open('text_country.txt') as f:
#     for line in f:
#         n, p = line.split('\t')
#         if n.startswith('G') and int(p) > 500000:
#             print(n)
