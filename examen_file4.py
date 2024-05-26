# Вам доступен текстовый файл words.txt со словами, разделенными пробелом.
# Напишите программу, которая находит и выводит самые длинные слова этого файла,
# не меняя порядка их следования

with open('words.txt', 'r', encoding='utf-8') as file:
    lst_file = file.read().split()
    max_len_word = max([len(word) for word in lst_file])
    for word in lst_file:
        if len(word) == max_len_word:
            print(word)
