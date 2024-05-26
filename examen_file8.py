# На вход программе подается строка текста с именем текстового файла,
# в котором написан код на языке Python. Напишите программу,
# выводящую на экран имена всех функций, для которых отсутствует
# поясняющий комментарий. Будем считать, что любая строка, начинающаяся
# со слова def и пробела, является началом определения функции.
# Функция содержит комментарий, если первый символ предыдущей строки - #.


with open('text_def_examen.txt', 'r', encoding='utf-8') as file:
    str_file = file.readlines()
    str_file_num = ['A']
    str_file_num.extend(str_file)
    lst_result = []
    for num in range(1, len(str_file_num)):
        if str_file_num[num][:3] == 'def' and str_file_num[num-1][0] != '#':
            lst_result.append(str_file_num[num])
    print(lst_result)
    if len(lst_result) > 1:
        lst_result = [el.strip(':\n').replace('def ', '') for el in lst_result]
        for name in lst_result:
            n = name.find('(')
            print(name[:n])
    else:
        print('Best Programming Team')

    print(lst_result)
