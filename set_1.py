# Даны по 10-балльной шкале оценки по информатике трех учеников.
# Напишите программу, выводящую множество оценок, которые есть и у
# первого, и у второго учеников, но которых нет у третьего ученика.


s1 = set(int(i) for i in '3 4 5 6 2 10 3 9 8 8'.split())
s2 = set(int(i) for i in '5 7 8 9 2 7 4 6 8 2'.split())
s3 = set(int(i) for i in '2 6 7 1 3 6 5 9 2 6'.split())

myset3 = s1.intersection(s2)
myset4 = myset3.difference(s3)
print(*sorted(myset4, reverse=True))
