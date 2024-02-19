stroka = '()()()'
s1 = stroka.replace('()', '')
# print(s1)
while '()' in stroka:
    stroka = stroka.replace('()', '')

print(stroka)


def skobka(stroka):
    while '()' in stroka:
        stroka = stroka.replace('()', '')
    if stroka != '':
        return False
    else:
        return True


print(skobka(stroka))
