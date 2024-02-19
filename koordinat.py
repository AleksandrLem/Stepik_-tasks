quantity_num = int(input('количество точек: '))
num = [''.join(input(f'введите координаты: ')).split()
       for _ in range(quantity_num)]

print(num)
count_I = 0
count_II = 0
count_III = 0
count_IV = 0
for list_i in num:
    if int(list_i[0]) > 0 and int(list_i[1]) > 0:
        count_I += 1
    elif int(list_i[0]) < 0 and int(list_i[1]) > 0:
        count_II += 1
    elif int(list_i[0]) < 0 and int(list_i[1]) < 0:
        count_III += 1
    elif int(list_i[0]) > 0 and int(list_i[1]) < 0:
        count_IV += 1

print('Первая четверть:', count_I)
print('Вторая четверть:', count_II)
print('Третья четверть:', count_III)
print('Четвертая четверть:', count_IV)


# num = ['1 -3', '2 -5']
# num_0 = ', '.join(num)
# print(num_0)
# num_1 = []
# num_2 = []
# for i in num:
#     # i.replace(' ', '')
#     num_1.append(i.split())

# print(num_1)
# for lst_i in num_1:
#     for j in lst_i:
#         num_2.append(int(j))

# print(num_2)
