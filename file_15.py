# Надо вывести цвета тех козлов, численность которых более 7% от общего кол-ва.

with open('goats.txt', 'r', encoding='utf-8') as file_inpt, \
        open('answer.txt', 'w', encoding='utf-8') as file_otpt:
    # список всех строк текста
    lst_file = [line.strip() for line in file_inpt]
    # словарь с цветами козлов
    dct_color = {}
    for line in lst_file[1:]:
        if line == 'GOATS':
            break
        else:
            dct_color[line] = 0
    # находим индекс, с которого начинется список козлов
    n = lst_file.index('GOATS')
    # список всех козлов
    lst_goats = []
    for line in lst_file[n+1:]:
        lst_goats.append(line)
    # количество всех козлов
    all_goats = len(lst_goats)
    # 7% от всего количества
    procent_7 = int(all_goats*0.07)
    # считаем всех козлов по цветам
    for line in lst_goats:
        dct_color[line] += 1
    # находим цвета козлов, которых больше 7% и добавляем их в итоговый список
    lst_result = []
    for key, value in dct_color.items():
        if value > procent_7:
            lst_result.append(key)
    # сортируем по алфавиту итоговый список
    lst_result = sorted(lst_result)
    # разбиваем список на строки
    lst_result = '\n'.join(lst_result)
    # записываем итоги в файл
    file_otpt.writelines(lst_result)

# короткое решение
with open('goats.txt') as f1, open('answer.txt', 'w') as f2:
    cont = f1.read().split('\n')
    colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
    print(*sorted(filter(lambda x: goats.count(x) /
          len(goats) > 0.07, colors)), sep='\n', file=f2)

# короткое решение через словари
with open('goats.txt', 'rt', encoding='utf-8') as fg1, \
        open('answer.txt', 'wt', encoding='utf-8') as ans1:
    goats = {}
    for line in fg1:
        goats[line.strip()] = goats.get(line.strip(), -1) + 1
    total = sum(goats.values())
    for k, v in goats.items():
        if v > total*0.07:
            print(k, file=ans1)
