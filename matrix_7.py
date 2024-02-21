n = 4  # int(input('matrix_size = '))
matrix = [['1', '2', '3', '4'],
          ['5', '6', '7', '8'],
          ['9', '10', '11', '12'],
          ['13', '14', '15', '16']]  # [input('row = ').split() for _ in range(n)]
print(matrix)

sum_upper = 0
sum_lower = 0
sum_left = 0
sum_right = 0

for rows in range(n):
    for cols in range(n):
        # Левая четверть
        if rows > cols and rows < n-1-cols:
            sum_left += int(matrix[rows][cols])
        # Правая четверть
        elif rows < cols and rows > n-1-cols:
            sum_right += int(matrix[rows][cols])
        # Верхняя четверть
        elif rows < cols and rows < n-1-cols:
            sum_upper += int(matrix[rows][cols])
        # Нижняя четверть
        elif rows > cols and rows > n-1-cols:
            sum_lower += int(matrix[rows][cols])

print('Верхняя четверть:', sum_upper)
print('Правая четверть:', sum_right)
print('Нижняя четверть:', sum_lower)
print('Левая четверть:', sum_left)
