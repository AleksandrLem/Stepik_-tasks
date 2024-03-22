import pprint
num = 5
s1 = 'Змея: язык программирования Python'.replace(':', '').split()
s2 = 'Баг: от англ. bug — жучок, клоп, ошибка в программе'.replace(':', '').split()
s3 = 'Конфа: конференция'.replace(':', '').split()
s4 = 'Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода'.replace(':', '').split()
s5 = 'Бета: бета-версия, приложение на стадии публичного тестирования'.replace(':', '').split()

sl1 = 'Змея'.title()
sl2 = 'Жаба'.title()
sl3 = 'костыль'.title()


lst_words = [s1, s2, s3, s4, s5]
#inp = [[i for i in input().replace(':', '').split()] for i in range(num)]
dict_words = {}


for el in lst_words:
    dict_words[el[0]] = ' '.join(el[1:])

#pprint.pprint(dict_words)

# # создаем список со списками определений, полученных на вводе
# n = int(input())
# lst_words = [[i for i in input().replace(':', '').split()] for i in range(n)]

# # создаем словарь
# dict_words = {}
# for el in lst_words:
#     dict_words[el[0]] = ' '.join(el[1:])

# # создаем список из слов для запроса
# m = int(input())
# lst_word = [[i for i in input().title().split()] for i in range(m)]
# print(lst_word)

lst_word = [sl1, sl2, sl3]

for el in lst_word:
    print(dict_words.get(el, 'Не найдено'))
