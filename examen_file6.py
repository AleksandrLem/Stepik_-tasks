# На вход программе подается строка текста с именем текстового файла.
# Напишите программу, выводящую на экран содержимое этого файла,
# но с заменой всех запрещенных слов звездочками *
# (количество звездочек равно количеству букв в слове).

# Запрещенные слова, разделенные символом пробела, хранятся в
# текстовом файле forbidden_words.txt. Гарантируется, что все
# слова в этом файле записаны в нижнем регистре.


with open('forbidden_words.txt', 'r', encoding='utf-8') as file, open('data_e.txt', 'r', encoding='utf-8') as datafile:
    stop_list = file.read().split()  # список стоп-слов
    strg_data = datafile.read()  # - исходная строка
    # strg_data_change - строка, где заменим стоп-слова на *
    strg_data_change = strg_data.lower()
    for word in stop_list:
        strg_data_change = strg_data_change.replace(word, '*'*len(word))
    result_strg = ''  # итоговая строка
    for el in range(len(strg_data_change)):
        if strg_data_change[el] == '*':
            result_strg += '*'
        else:
            result_strg += strg_data[el]
    print(result_strg)


# stop_list = 'hello email python the exam wor is'.split()
# strg = 'Hello, world! Python IS the programming language of thE future. My EMAIL is....PYTHON is awesome!!!!'
# print(strg)
# print(stop_list)
# strg1 = strg.lower()
# for word in stop_list:
#     strg1 = strg1.replace(word, '*'*len(word))
# print(strg1)
# new_str = ''
# for el in range(len(strg1)):
#     if strg1[el] == '*':
#         new_str += '*'
#     else:
#         new_str += strg[el]
# print(new_str)
