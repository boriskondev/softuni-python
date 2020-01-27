matrix = []
max_killed = 0
max_killed_coords = 0
knights_removed = 0


def check_index(matrix_row, matrix_col, array):
    if 0 <= matrix_row < len(array) and 0 <= matrix_col < len(array[0]):
        return True
    return False


def check_move(matrix_row, matrix_col, array):
    killed = 0
    if check_index(matrix_row - 1, matrix_col + 2, array):
        if array[matrix_row - 1][matrix_col + 2] == "K":
            killed += 1
    if check_index(matrix_row + 1, matrix_col + 2, array):
        if array[matrix_row + 1][matrix_col + 2] == "K":
            killed += 1
    if check_index(matrix_row + 2, matrix_col + 1, array):
        if array[matrix_row + 2][matrix_col + 1] == "K":
            killed += 1
    if check_index(matrix_row + 2, matrix_col - 1, array):
        if array[matrix_row + 2][matrix_col - 1] == "K":
            killed += 1
    if check_index(matrix_row - 1, matrix_col - 2, array):
        if array[matrix_row - 1][matrix_col - 2] == "K":
            killed += 1
    if check_index(matrix_row + 1, matrix_col - 2, array):
        if array[matrix_row + 1][matrix_col - 2] == "K":
            killed += 1
    if check_index(matrix_row - 2, matrix_col - 1, array):
        if array[matrix_row - 2][matrix_col - 1] == "K":
            killed += 1
    if check_index(matrix_row - 2, matrix_col + 1, array):
        if array[matrix_row - 2][matrix_col + 1] == "K":
            killed += 1
    return killed


matrix_size = int(input())

for row in range(matrix_size):
    matrix.append([x for x in input()])

while True:
    max_killed = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "K":
                killed_now = check_move(row, col, matrix)
                if killed_now > max_killed:
                    max_killed = killed_now
                    max_killed_coords = (row, col)
    if max_killed == 0:
        break
    matrix[max_killed_coords[0]][max_killed_coords[1]] = "0"
    knights_removed += 1

print(knights_removed)

