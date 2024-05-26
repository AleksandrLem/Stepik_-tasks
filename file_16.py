# На вход программе подается натуральное число n и n строк с названиями файлов.
# Напишите программу, которая создает файл output.txt и выводит в него
# содержимое всех файлов, не меняя их порядка.


# список файлов
lst_file = [input('название файла: ')
            for _ in range(int(input('количество файлов: ')))]


# функция для чтения списка файлов и записи в итоговый файл
def open_file(lst=None):
    all_lst = []  # итоговый список со строками из всех файлов
    # проходим по списку с названиями файлов
    for line in lst:
        # читаем файл
        with open(line, 'r', encoding='utf-8') as file:
            # создаем список строк файла
            lst_file = [el for el in file]
            # добавляем список строк в итоговый список
            all_lst.extend(lst_file)
    # записываем в итоговый файл все строки из списка all_lst
    with open('output.txt', 'w', encoding='utf-8') as out_file:
        out_file.writelines(all_lst)


open_file(lst_file)


# РЕШЕНИЕ АВТОРА ЗАДАЧИ

# input_files_number = int(input())
# # здесь мы будем хранить имена всех файлов, из которых нам нужно взять содержимое
# input_files = [input() for _ in range(input_files_number)]

# with open("output.txt", "w", encoding="utf-8") as output_f:
#     for input_file in input_files:  # проходим по всем файлам
#         with open(input_file, "r", encoding="utf-8") as input_f:
#             file_contents = input_f.read()  # считываем содержимое файла
#             output_f.write(file_contents)  # записываем содержимое файла
