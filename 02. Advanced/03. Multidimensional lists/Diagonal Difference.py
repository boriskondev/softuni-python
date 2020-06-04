matrix = []
left_diagonal = 0
right_diagonal = 0

matrix_size = int(input())

for row in range(matrix_size):
    matrix.append(list(map(int, input().split())))

r_count = matrix_size - 1

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if row == col:
            left_diagonal += matrix[row][col]
        if col == r_count:
            right_diagonal += matrix[row][col]
            r_count -= 1

print(abs(left_diagonal - right_diagonal))