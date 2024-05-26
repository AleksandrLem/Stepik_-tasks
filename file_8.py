with open('text_num.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = sum([int(num) for num in line.split()])
        print(line)
