# Вам доступен текстовый файл logfile.txt с информацией о времени входа
# пользователя в систему и выхода из нее. Каждая строка файла содержит
# три значения, разделенные запятыми и символом пробела: имя пользователя,
# время входа, время выхода, где время указано в 24-часовом формате.

# Напишите программу, которая создает файл output.txt и выводит в
# него имена всех пользователей (не меняя порядка следования),
# которые были в сети не менее часа.

with open('logfile.txt', 'r', encoding='utf-8') as hour_time, open('output.txt', 'w', encoding='utf-8') as name_file:
    # список со списками строк
    s = [line.strip().split(',') for line in hour_time]
    # проходим циклом и вытаскиваем время из списка со строкой, считаем количество минут
    for lst in s:
        h1, m1 = [int(num) for num in lst[1].strip().split(':')]
        h2, m2 = [int(num) for num in lst[2].strip().split(':')]
        t_hour = (h2*60+m2) - (h1*60+m1)
        # записываем нужные имена в файл output.txt
        if t_hour >= 60:
            name_file.write(f'{lst[0]}\n')


# решение через datetime
# from datetime import datetime

# with open('logfile.txt', encoding='utf-8') as logfile, open('output.txt', 'w') as output:
#     for log in logfile.read().split('\n'):
#         name, first_time, second_time = log.split(', ')
#         delta = datetime.strptime(second_time, "%H:%M") - datetime.strptime(first_time, "%H:%M")
#         if delta.seconds >= 3600:
#             print(name, file=output)
