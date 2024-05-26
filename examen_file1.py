# На вход программе подается строка текста с именем текстового файла.
# Напишите программу для вывода на экран количества строк данного файла.

stg = input('name file: ')

with open(stg, 'r', encoding='utf8') as file:
    quantity = len([line for line in file])
    print(quantity)
