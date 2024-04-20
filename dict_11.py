# На вход программе подается список стран и городов каждой страны.
# Затем даны названия городов. Напишите программу, которая для каждого
# города выводит, в какой стране он находится.

# Формат входных данных
# Программа получает на вход количество стран n. Далее идет n строк,
# каждая строка начинается с названия страны, затем идут названия городов
# этой страны. В следующей строке записано число m, далее идут m
# запросов — названия каких-то mm городов, из перечисленных выше.

# Формат выходных данных
# Программа должна вывести название страны, в которой находится
# данный город в соответствии с примером.



# s1 = 'Германия Берлин Мюнхен Гамбург Дортмунд'.split()

# s11 = dict.fromkeys(s1[1:], s1[0])
# print(s11)
# print(s11.get('Мюнхен', 'нет такого ключа'))



# количество строк с городами и странами
country_count = int(input())

# создаем список со списками городов и стран
country_city = [[j for j in input().split()] for i in range(country_count)]

# итоговый словарь, где ключом будут города, а значение страны
dict_result = {}

# проходим циклом по списку и заполняем словарь dict_result
for el in country_city:
    dict_city = dict.fromkeys(el[1:], el[0])
    dict_result.update(dict_city)

# количество городов
city_count = int(input())

# создаем список с городами
city_lst = [input() for i in range(city_count)]

# проходим по списку городов (ключ - это город) и выводим значение (название страны)
for city in city_lst:
    print(dict_result.get(city, 'нет такого ключа'))


# Короткое решение
# my_dict = {i[0]:i[1:] for i in [input().split() for j in range(int(input()))]}
# cities = [input() for i in range(int(input()))]
# for i in cities:
#     for key, value in my_dict.items():
#         if i in value:
#             print(key)


# Ещё решение
# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])