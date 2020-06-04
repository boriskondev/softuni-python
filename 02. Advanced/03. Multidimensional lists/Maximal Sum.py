matrix = []
current_sum, max_sum, max_row, max_col = 0, 0, 0, 0

matrix_rows, matrix_cols = map(int, input().split())

for row in range(matrix_rows):
    matrix.append(list(map(int, input().split())))

for row in range(matrix_rows - 2):
    for col in range(matrix_cols - 2):
        current_sum = sum([sum(sub_row[col:col + 3]) for sub_row in matrix[row:row + 3]])
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_col = col

print(f"Sum = {max_sum}")
for row in range(max_row, max_row + 3):
    for col in range(max_col, max_col + 3):
        print(matrix[row][col], end=" ")
    print()