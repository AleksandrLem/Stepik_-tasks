# Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt.

txt_line = input('введите любой текст: ')
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(txt_line)

# второй способ
print(input('введите текст: '), file=open('output.txt', 'w', encoding='utf-8'))
