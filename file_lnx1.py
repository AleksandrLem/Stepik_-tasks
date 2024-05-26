with open('Stepik_tasks/nums.txt', 'r', encoding='utf-8') as file:

    lst_num = []
    s = 0
    # проходим по всем строкам и меняем буквы на пробелы
    # добавляем исправленную строку в список
    for line in file:
        for el in line:
            if el not in '0123456789':
                line = line.replace(el, ' ')
        lst_num.append(line)
    # проходим по списку и вычисляем сумму чисел
    for num in lst_num:
        s += sum([int(n) for n in num.split()])
    print(s)


# короткое решение
with open('Stepik_tasks/nums.txt', encoding='utf-8') as file:

    row = ''.join(c if c.isdigit() else ' ' for c in file.read())
    print(row)
    print(sum(map(int, row.split())))