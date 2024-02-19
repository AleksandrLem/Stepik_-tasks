l1 = []
l2 = []
l3 = []
l4 = []

s1 = l1.extend('012345')
s2 = l2.extend('0236')
s3 = l3.extend('03452222')
s4 = l4.extend('9302')

s1 = set(l1)
s2 = set(l2)
s3 = set(l3)
s4 = set(l4)

s7 = s1 & s2 & s3 & s4

print(s1)
print(s2)
print(s3)
print(s4)

print(*sorted(s7))

# На вход программе подается натуральное число n, а затем
# n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит все общие цифры в порядке
# возрастания у всех введенных чисел.

lst_num = [set(input('num = ')) for _ in range(int(input('n = ')))]
print(lst_num)
set1 = lst_num[0]
for i in lst_num:
    set1 &= i
print(*sorted(set1))

''' можно решить так: '''
# n = int(input())
# numbers = [input() for _ in range(n)]
# num_set = set(numbers[0]).intersection(*numbers)
# print(*sorted(num_set))
