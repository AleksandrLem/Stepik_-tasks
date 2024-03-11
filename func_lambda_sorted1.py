# Список data содержит информацию о численности населения некоторых штатов США.
# Напишите программу сортировки по убыванию списка data на основании последнего
# символа в названии штата. Затем распечатайте элементы этого списка, каждый
# на новой строке в формате:

# <название штата>: <численность населения>

# Сортировка производится в лексикографическом порядке (по алфавиту) по убыванию
# на основании последнего символа в названии штата. При этом, если два штата имеют
# одинаковый последний символ, следует сохранить их взаиморасположение в начальном списке.

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
        (1805832, 'West Virginia'), (39865590,
                                     'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
        (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281,
                                                         'Washington'), (7151502, 'Arizona'),
        (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

# Сортируем список, в качестве ключа берем элемент картежа с названием штата,
# далее берем последний символ в названии этого штата, затем применяем reverse для
# сортировки в обратном порядке

# Применяем функцию map, чтобы высетси элементы списка согласно условию:
# первым идет название штата, затем двоеточие и численность населения

data1 = sorted(data, key=lambda el: el[1][-1], reverse=True)
data2 = map(lambda el: f'{el[1]}: {el[0]}', data1)

print(*data2, sep='\n')
