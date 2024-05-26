# Вам доступен текстовый файл text_price.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:

# наименование товара;
# количество товара (целое число);
# цена (в рублях) товара за 1 шт (целое число).
# Напишите программу, выводящую на экран общую стоимость заказа.


file = open('text_price.txt', 'r', encoding='utf-8')
# приводим строки к виду [['телефон', '4', '12500'], ['бургер', '1', '500']]
file_lst = [line.replace('\t', ' ').strip().split()
            for line in file.readlines()]
print(file_lst)
# вычисляем стоимость в каждом списке, затем общую сумму
file_lst = sum([int(lst[1])*int(lst[2]) for lst in file_lst if len(lst) > 0])
print(file_lst)

file.close()

# решение черем map и lambda
file = open('text_price.txt', 'r', encoding='utf-8')
lines = map(str.split, file)
print(lines)
print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
file.close()
