word = '*!*!*?'
dct = {'а': 3, 'н': 2, 'с': 1}

d1 = 'а: 3'.split(':')
print(d1)


dct1 = {v: k for k, v in dct.items()}
print(dct1)

# for simbol in word:
#     result[simbol] = result.get(simbol, 0) + 1

for el in word:
    print(dct1[word.count(el)], end='')
print()

'''Решение для степика с вводом данных'''
# # принимаем входные данные
# word = input()
# n = int(input())
# strg =[input().split(':') for i in range(n)]

# # создаем словарь, где ключ - число, значение - символ
# dct = {}
# for el in strg:
#     dct[int(el[1].lstrip())] = el[0]

# # выводим расшифровку
# for el in word:
#     print(dct[word.count(el)], end='')
