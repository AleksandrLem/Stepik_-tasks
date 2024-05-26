# Вам доступен текстовый файл input.txt, состоящий из нескольких строк.
# Напишите программу для записи содержимого этого файла в файл output.txt
# в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел.
# Нумерация строк должна начинаться с 1.


with open('input.txt', 'r', encoding='utf-8') as file_inp, open('output_moe.txt', 'w', encoding='utf-8') as file_out:
    # создаем список строк файла input.txt
    lst_file = [line for line in file_inp]
    # добавляем нумерацию в строки
    lst_file = [
        f"{str(n+1)}) {lst_file[n]}" for n in range(len(lst_file))]
    # записываем нумерованный список в файл output.txt
    file_out.writelines(lst_file)

# короткое решение
with open('input.txt') as inp, open('output.txt', 'w') as out:
    for i, j in enumerate(inp, start=1):
        print(f'{i}) {j}', end='', file=out)
