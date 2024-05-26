# На вход программе подается строка текста с именем текстового файла.
# Напишите программу, выводящую на экран последние
# 10 строк данного файла.

with open('text_exam.txt', 'r', encoding='utf-8') as file:
    lst_file = [line.strip() for line in file]
    print(*lst_file[-10:], sep='\n')
