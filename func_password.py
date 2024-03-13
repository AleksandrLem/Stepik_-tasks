# Хороший пароль по условиям этой задачи состоит как минимум из
# 7 символов, содержит хотя бы одну цифру, заглавную и строчную букву.
# Напишите программу со встроенной функцией any() для определения хорош ли
# введенный пароль.


s = 'abcABC9'


s_len = len(s)>=7 # 7 символов
s_lower = any(map(lambda el: el.islower(), s)) # содержит ли строчную букву
s_upper = any(map(lambda el: el.isupper(), s)) # содержит ли заглавную букву
s_digit = any(map(lambda el: el.isdigit(), s)) # содержит ли хотя бы одну цифру
print(s_lower, s_upper, s_digit, s_len)

# добавим все условия в список и проверим с помощью функции all
password_ok = all([any(map(lambda el: el.islower(), s)),
                   any(map(lambda el: el.isupper(), s)),
                   any(map(lambda el: el.isdigit(), s)),
                   len(s)>=7])
print('YES' if password_ok else 'NO')