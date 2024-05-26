def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        # читаем файл и создаем список со списками строк
        lst_file = [line.strip().split(',') for line in file]
        # print(lst_file)
        lst_result = []  # итоговый список, будем добавлять в него словари
        # проходим по списку lst_file циклом, начиная со 2-й строки, т.к.
        # первая строка - это список элементов, которые нужны для создания ключей словаря
        # перебираем строки, начиная со 2-й, и при каждом обходе строки создаем словарь,
        # используя генератор словарей, где в качестве последовательности
        # будет zip(lst_file[0], line) - здесь lst_file[0] - это первая строка
        # line - это текущая строка цикла,
        # ключами назначаем элементы списка lst_file[0], а значением -
        # элементы списка line
        # добавляем полученный словарь dct_key в итоговый список lst_result
        for line in lst_file[1:]:
            dct_key = {key: value for key, value in zip(lst_file[0], line)}
            lst_result.append(dct_key)
        return lst_result  # возвращаем итоговый список


print(read_csv())

# короткое решение
# def read_csv():
#     with open('data.csv') as file:
#         keys = file.readline().strip().split(',')
#         return [dict(zip(keys, line.strip().split(','))) for line in file]
