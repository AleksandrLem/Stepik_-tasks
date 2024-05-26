# Транслитерация — передача знаков одной письменности знаками другой письменности,
# при которой каждый знак (или последовательность знаков) одной системы письма
# передаётся соответствующим знаком (или последовательностью знаков) другой системы письма.

# Вам доступен текстовый файл cyrillic.txt, содержащий текст. Напишите программу для
# транслитерации этого файла, то есть замены кириллических символов на латинские
# в соответствии с предложенной таблицей. Все остальные символы надо оставить без изменений.
# Результат транслитерации требуется записать в файл transliteration.txt.


translate_dict = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
    'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
    'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*',
    'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je',
    'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya',
}

str1 = 'Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР. \
We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.'
str2 = ''

for key, value in translate_dict.items():
    str1 = str1.replace(key, value)
print(str1)
print()

with open('cyrillic.txt', 'r', encoding='utf-8') as file, open('transliteration.txt', 'w', encoding='utf-8') as transl_file:
    str_file = file.read()
    print(str_file)
    print()
    for key, value in translate_dict.items():
        str_file = str_file.replace(key, value)
    print(str_file)
    transl_file.write(str_file)
