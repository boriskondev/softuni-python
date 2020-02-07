def print_matrix(array):
    for r in array:
        print(" ".join(r))
    print()


def check_index(matrix_row, matrix_col, array):
    if 0 <= matrix_row < len(array) and 0 <= matrix_col < len(array[0]):
        return True
    return False


def award_everyone(matrix_row, matrix_col, array, gifts, good_kids):
    for r in range(matrix_row - 2, matrix_row + 1):
        for c in range(matrix_col - 1, matrix_col + 2):
            if array[r][c] == "X":
                gifts -= 1
                array[r][c] = "-"
            elif array[r][c] == "V":
                gifts -= 1
                good_kids -= 1
                array[r][c] = "-"
    print_matrix(array)
    print()


def move_up(matrix_row, matrix_col, array, gifts, good_kids):
    if check_index(matrix_row - 1, matrix_col, array):
        if array[matrix_row - 1][matrix_col] == "V":
            gifts -= 1
            good_kids -= 1
            array[matrix_row - 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row - 1][matrix_col] == "X":
            array[matrix_row - 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row - 1][matrix_col] == "C":
            array[matrix_row - 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
            award_everyone(matrix_row, matrix_col, array, gifts, good_kids)
        elif array[matrix_row - 1][matrix_col] == "-":
            array[matrix_row - 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
        print_matrix(array)
        return matrix_row, matrix_col, array, gifts, good_kids


def move_right(matrix_row, matrix_col, array, gifts, good_kids):
    if check_index(matrix_row, matrix_col + 1, array):
        if array[matrix_row][matrix_col + 1] == "V":
            gifts -= 1
            good_kids -= 1
            array[matrix_row][matrix_col + 1] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row][matrix_col + 1] == "X":
            array[matrix_row][matrix_col + 1] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row][matrix_col + 1] == "C":
            array[matrix_row][matrix_col + 1] = "S"
            array[matrix_row][matrix_col] = "-"
            award_everyone(matrix_row, matrix_col, array, gifts, good_kids)
        elif array[matrix_row][matrix_col + 1] == "-":
            array[matrix_row][matrix_col + 1] = "S"
            array[matrix_row][matrix_col] = "-"
        print_matrix(array)


def move_down(matrix_row, matrix_col, array, gifts, good_kids):
    if check_index(matrix_row + 1, matrix_col, array):
        if array[matrix_row + 1][matrix_col] == "V":
            gifts -= 1
            good_kids -= 1
            array[matrix_row + 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row + 1][matrix_col] == "X":
            array[matrix_row + 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row + 1][matrix_col] == "C":
            array[matrix_row + 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
            award_everyone(matrix_row, matrix_col, array, gifts, good_kids)
        elif array[matrix_row + 1][matrix_col] == "-":
            array[matrix_row + 1][matrix_col] = "S"
            array[matrix_row][matrix_col] = "-"
        print_matrix(array)


def move_left(matrix_row, matrix_col, array, gifts, good_kids):
    if check_index(matrix_row, matrix_col - 1, array):
        if array[matrix_row][matrix_col - 1] == "V":
            gifts -= 1
            good_kids -= 1
            array[matrix_row][matrix_col - 1] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row][matrix_col - 1] == "X":
            array[matrix_row][matrix_col - 1] = "S"
            array[matrix_row][matrix_col] = "-"
        elif array[matrix_row][matrix_col - 1] == "C":
            array[matrix_row][matrix_col - 1] = "S"
            array[matrix_row][matrix_col] = "-"
            award_everyone(matrix_row, matrix_col, array, gifts, good_kids)
        elif array[matrix_row][matrix_col - 1] == "-":
            array[matrix_row][matrix_col - 1] = "S"
            array[matrix_row][matrix_col] = "-"
        print_matrix(array)
    return matrix_row, matrix_col, array, gifts, good_kids


count_of_presents = int(input())
neighbourhood_size = int(input())

matrix = []
santa_position = ()
nice_kids = 0
nice_kids_left = 0

for _ in range(neighbourhood_size):
    matrix.append(input().split())

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "S":
            santa_position = row, col
        if matrix[row][col] == "V":
            nice_kids += 1

while True:
    print(f"Presents: {count_of_presents}")
    command = input()
    if command == "Christmas morning":
        break
    elif command == "up":
        move_up(santa_position[0], santa_position[1], matrix, count_of_presents, nice_kids)
    elif command == "down":
        move_down(santa_position[0], santa_position[1], matrix, count_of_presents, nice_kids)
    elif command == "left":
        move_left(santa_position[0], santa_position[1], matrix, count_of_presents, nice_kids)
    elif command == "right":
        move_right(santa_position[0], santa_position[1], matrix, count_of_presents, nice_kids)
    if count_of_presents == 0:
        break
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "S":
                santa_position = row, col

if nice_kids_left > 0 and count_of_presents == 0:
    print("Santa ran out of presents!")


for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "V":
            nice_kids_left += 1

print_matrix(matrix)

if nice_kids_left == 0 and count_of_presents >= 0:
    print(f"Good job, Santa! {nice_kids - nice_kids_left} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")
