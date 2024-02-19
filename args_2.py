def print_products(*args):
    count = 0
    for i in args:
        if type(i) == str and len(i) > 1:
            count += 1
            print(f'{count}) {i}')
    if count == 0:
        print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',),
               'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
