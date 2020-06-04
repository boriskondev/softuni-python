matrix_size = int(input())

matrix = []

for row in range(matrix_size):
    matrix.append(list(map(int, input().split())))

sum_diag = 0

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if row == col:
            sum_diag += matrix[row][col]

print(sum_diag)