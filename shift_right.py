# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел. Напишите
# программу циклического сдвига элементов списка направо,
# когда последний элемент становится первым, а остальные сдвигаются
# на одну позицию вперед, в сторону увеличения индексов.

st = '1 2 3 4 5'.split()
print(st[-1], *st[:-1])