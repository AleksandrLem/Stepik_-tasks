# Вам доступен текстовый файл grades.txt, содержащий оценки студента за
# три теста в каждом из триместров. Строки файла имеют вид:
# фамилия оценка_1 оценка_2 оценка_3.

# Напишите программу для подсчета количества студентов, сдавших все три теста.
# Тест считается сданным, если количество баллов по нему не меньше 65.


with open('grades.txt', 'r', encoding='utf-8') as file:
    lst_file = [line.strip().split() for line in file]
    quantity = 0
    for lst in lst_file:
        if all(map(lambda x: True if int(x) >= 65 else False, lst[1:])):
            quantity += 1

    print(quantity)
