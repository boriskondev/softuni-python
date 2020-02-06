def print_matrix(array):
    for r in array:
        print(" ".join(r))


def check_index(matrix_row, matrix_col, array):
    if 0 <= matrix_row < len(array) and 0 <= matrix_col < len(array[0]):
        return True
    return False


def award_everyone(matrix_row, matrix_col, array, gifts):
    for r in range(matrix_row - 2, matrix_row + 1):
        for c in range(matrix_col - 1, matrix_col + 2):
            if array[r][c] == "V" or array[r][c] == "X":
                gifts -= 1
                array[r][c] = "-"
                # print_matrix(array)
                # print()


def move_up(matrix_row, matrix_col, array, gifts):
    if check_index(matrix_row - 1, matrix_col, array):
        if array[matrix_row - 1][matrix_col] == "V":
            gifts -= 1
            array[matrix_row - 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row - 1][matrix_col] == "X":
            array[matrix_row - 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row - 1][matrix_col] == "C":
            array[matrix_row - 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
            # print_matrix(array)
            # award_everyone(matrix_row, matrix_col, array, gifts)


count_of_presents = int(input())
neighbourhood_size = int(input())

matrix = []
santa_position = ()

for _ in range(neighbourhood_size):
    matrix.append(input().split())

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "S":
            santa_position = row, col

while True:
    command = input()
    if command == "Christmas morning":
        break
    elif command == "up":
        move_up(santa_position[0], santa_position[1], matrix, count_of_presents)
    elif command == "down":
        pass
    elif command == "left":
        pass
    elif command == "right":
        pass