
def game_knb(timur, ruslan):
    k = 'камень'
    n = 'ножницы'
    b = 'бумага'
    # ничья
    if (timur == k and ruslan == k) or (timur == n and ruslan == n) or (timur == b and ruslan == b):
        return 'ничья'
    # камень ножницы
    elif timur == k and ruslan == n:
        return 'Тимур'
    elif timur == n and ruslan == k:
        return 'Руслан'
    # камень бумага
    elif timur == k and ruslan == b:
        return 'Руслан'
    elif timur == b and ruslan == k:
        return 'Тимур'
    # ножницы бумага
    elif timur == n and ruslan == b:
        return 'Тимур'
    elif timur == b and ruslan == n:
        return 'Руслан'


t = input('t = ')
r = input('r = ')

print(game_knb(t, r))
