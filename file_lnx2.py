# Вам доступен текстовый файл file.txt, набранный латиницей.
# Напишите программу, которая выводит количество букв латинского
# алфавита, слов и строк.



with open('Stepik_tasks/file.txt', 'r', encoding='utf-8') as file:
    # количество строк
    lines = len(file.readlines())
    file.seek(0) # возвращаем курсор в начало
    set_file = file.read().split()
    # количество слов
    words = len(sorted([word.strip('."').lower() for word in set_file]))

    file.seek(0)# возвращаем курсор в начало
    letters = file.read()
    # количество слов
    letters = len([el for el in letters if el.isalpha()])

    print('Input file contains:')
    print(letters, 'letters')
    print(words, 'words')
    print(lines, 'lines')

# короткое и простое решение
with open('Stepik_tasks/file.txt') as f:
    txt = f.read()
    print('Input file contains:')
    print(sum(map(str.isalpha, txt)), 'letters')
    print(len(txt.split()), 'words')
    print(txt.count('\n') + 1, 'lines')