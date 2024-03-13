# Напишите программу для вычисления и вывода суммы квадратов двузначных чисел,
# которые делятся на 7 без остатка.

# Примечание 1. При решении задачи используйте функции filter(), map() и sum().

# Примечание 2. На 7 должно делиться исходное двузначное число, а не его квадрат.

# Примечание 3. Не забывайте про отрицательные двузначные числа.

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228,
           51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183,
           266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92,
           286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
           187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65,
           135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228,
           129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276,
           4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
           10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]


# функция для вывода двузначного числа, которое делится на 7 без остатка
def num_two_seven(num):
    return (10 <= num <= 99 or -99 <= num <= -10) and num % 7 == 0


# функция для вычисления квадрата числа
def square(num):
    return num**2


# фильтруем список (только двузначные числа, котрые делятся на 7 без остатка)
numbers_seven = filter(num_two_seven, numbers)
print(numbers_seven)


# находим квадраты каждого числа в списке
sq_lst = map(square, numbers_seven)
print(sq_lst)

# находим сумму предыдущего списка
print(sum(sq_lst))

# решение в одну строку
result = sum(map(square, filter(num_two_seven, numbers)))
print(result)