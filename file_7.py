with open('text_lines.txt', 'r', encoding='utf-8') as file:
    # создаем список строк
    file_lst = [line.strip() for line in file.readlines()]
    # находим максимальную длину строки во всём тексте
    max_len = max([len(l) for l in file_lst])
    # выводим строки, которые равны максимальной длине
    for line in file_lst:
        print(line) if len(line) == max_len else None
