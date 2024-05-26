# Вам доступен текстовый файл text_int1.txt. В файле записано два целых числа,
# они могут быть разделены символами пробела и конца строки.
# Напишите программу, выводящую на экран сумму этих чисел.

file = open('text_int1.txt', 'r', encoding='utf-8')

# создаем список строк, удаляем все пробелы
file_lst = [line.strip() for line in file.readlines()]
# удаляем все пустые строки '' из списка, оставляем только числа
file_lst = sum([int(el) for el in file_lst if el != ''])
print(file_lst)
file.close()

# простое короткое решение
file = open('text_int1.txt')
print(sum(map(int, file.read().split())))
file.close()
