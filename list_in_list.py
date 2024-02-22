# На вход программе подается строка текста, содержащая символы.
# Напишите программу, которая упаковывает последовательности
# одинаковых символов заданной строки в подсписки.

s = 'g i v e t h h i i s m a a a n a g u u n'.split()

lst_in = [[]]
for i in range(len(s)):
    if s[i]!=s[i-1]:
        lst_in.append([s[i]])
    else:
        lst_in[-1].append(s[i])
print(lst_in)
print()
if lst_in[0] == []:
    del lst_in[0]
print(lst_in)
