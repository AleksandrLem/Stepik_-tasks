# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел. Напишите программу,
# которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
# Если в списке нечетное количество элементов, то последний остается на своем месте.

def replacement(strg):
    strg = strg.split()
    lst = []
    for i in range(0, len(strg)-1, 2):
        lst.append(strg[i+1])
        lst.append(strg[i])
    if len(strg) % 2 != 0:
        lst.append(strg[-1])
        return ' '.join(lst)
    return ' '.join(lst)


print(replacement('1 2 3 4 5'))
print(replacement('2 3 2 4'))
print(replacement('1'))

# более простое решение
numbers = '3 5 6 8 1'.split()
for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(*numbers)
