n = 4  # int(input('matrix_size = '))
matrix = [['1', '2', '3', '4'],
          ['5', '6', '7', '8'],
          ['9', '10', '11', '12'],
          ['13', '14', '15', '16']]  # [input('row = ').split() for _ in range(n)]
print(matrix)

el_lst = []

for rows in range(n):
    for cols in range(n):
        if rows > cols and rows < n-1-cols:
            el_lst.append(int(matrix[rows][cols]))
        elif rows > cols and rows > n-1-cols:
            el_lst.append(int(matrix[rows][cols]))
        elif rows == cols:
            el_lst.append(int(matrix[rows][cols]))
        elif cols == n-rows-1 and rows > cols:
            el_lst.append(int(matrix[rows][cols]))
print(max(el_lst))


'''Решение без дополнительного списка'''
# n = int(input())
# matrix = []


# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)

# largest = matrix[0][0]

# for i in range(n):
#     for j in range(n):
#         if i >= j and matrix[i][j] > largest:
#             largest = matrix[i][j]

# print(largest)
