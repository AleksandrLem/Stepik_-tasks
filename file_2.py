# Вам доступен текстовый файл text_int.txt из двух строк, на каждой из них записано целое число.
# Напишите программу, выводящую на экран сумму этих чисел.

file = open('text_int.txt', 'r', encoding='utf-8')

file_lst = sum([int(line.rstrip()) for line in file.readlines()])
print(file_lst)

file.close()
