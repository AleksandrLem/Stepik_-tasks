# число без остатка делится на 19 или на 13
def func(num): return num % 19 == 0 or num % 13 == 0

# print(func(19))
# print(func(13))
# print(func(20))
# print(func(15))
# print(func(247))

# строка начинается и заканчивается на английскую a


def func(strg): return strg[0].lower() == 'a' and strg[-1].lower() == 'a'

# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))

# True - если число больше 0, False - если не число или меньше нуля


def is_non_negative_num(strg): return strg.replace('.', '', 1).isdigit()

# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))


# True - если num число, False - если num не число
def is_num(num):
    try:
        num = float(num)
        return True
    except ValueError:
        return False


print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
