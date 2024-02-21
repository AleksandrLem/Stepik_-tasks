n = int(input('количество строк: '))
m = int(input('количество столбцов: '))

matrix = []
lst_max = []

# формируем матрицу nxm
for _ in range(n):
    row = [int(i) for i in input('string = ').split()]
    matrix.append(row)
# можно матрицу сформировать таким образом:
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]

# формируем список из максимальных значений матрицы
for i in matrix:
    lst_max.append(max(i))
# находим строку с максимальным элементом
for i in range(len(lst_max)):
    if lst_max[i] == max(lst_max):
        line = i
        break
# находим столбец с максимальным элементом
for i in range(m):
    if matrix[line][i] == max(matrix[line]):
        column = i
        break
print(line, column)

# Короткое решение:
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# row, col = 0, 0

# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row,col = i, j

# print(row, col)
