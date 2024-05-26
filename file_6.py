with open('text_line.txt', 'r', encoding='utf-8') as file:
    file_lst = [line.strip() for line in file.readlines()]

    for n in range(len(file_lst)-1, -1, -1):
        print(file_lst[n])
