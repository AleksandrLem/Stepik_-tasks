# Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида:
# фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от
# 0 до 100 включительно.

# Напишите программу для добавления
# 5 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в файл new_scores.txt.

with open('class_scores.txt', 'r', encoding='utf-8') as file_inp, open('new_scores.txt', 'w', encoding='utf-8') as file_out:
    # создаем список строк файла input.txt
    lst_file = [line.strip().split() for line in file_inp]
    print(lst_file)
    lst_result = []
    for lst in lst_file:
        if 95 <= int(lst[1]) <= 100:
            num = 100 - int(lst[1])
            num = str(int(lst[1])+num) + '\n'
            lst_result.append([lst[0], num])
        else:
            num = str(int(lst[1])+5) + '\n'
            lst_result.append([lst[0], num])
    lst_result = [' '.join(lst) for lst in lst_result]
    print(lst_result)
    # записываем нумерованный список в файл output.txt
    file_out.writelines(lst_result)

# решение более простое и короткое
# with open('class_scores.txt') as class_scores, open('new_scores.txt', 'w') as new_scores:
#     for line in class_scores:
#         name, score = line.split()
#         score = int(score) + 5
#         if score > 100:
#             score = 100
#         print(name, score, file=new_scores)
