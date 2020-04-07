def print_matrix(array):
    for r in array:
        print(" ".join(r))


def check_around(r, c, array, gifts, good_kids):
    if array[r][c] == "X":
        gifts -= 1
        array[r][c] = "-"
    elif array[r][c] == "V":
        gifts -= 1
        good_kids += 1
        array[r][c] = "-"
    if gifts == 0:
        return array, gifts, good_kids
    return array, gifts, good_kids


def award_everyone(new_row, new_col, array, gifts, good_kids):
    coords_around = [
        [new_row - 1, new_col - 1],
        [new_row - 1, new_col],
        [new_row - 1, new_col + 1],
        [new_row, new_col + 1],
        [new_row + 1, new_col + 1],
        [new_row + 1, new_col],
        [new_row + 1, new_col - 1],
        [new_row, new_col - 1]
    ]

    for coords in coords_around:
        if check_index(coords[0], coords[1], array):
            array, gifts, good_kids = check_around(coords[0], coords[1], array, gifts, good_kids)
            if gifts == 0:
                return array, gifts, good_kids
    return array, gifts, good_kids


def prepare_for_action(com, position, array, gifts, good_kids):
    old_row, old_col = position[0], position[1]
    new_row, new_col = None, None
    if com == "up":
        new_row, new_col = position[0] - 1, position[1]
    elif com == "right":
        new_row, new_col = position[0], position[1] + 1
    elif com == "down":
        new_row, new_col = position[0] + 1, position[1]
    elif com == "left":
        new_row, new_col = position[0], position[1] - 1
    if check_index(new_row, new_col, array):
        position, array, gifts, good_kids = take_move(old_row, old_col, new_row, new_col, array, gifts, good_kids)
    return position, array, gifts, good_kids


def check_index(matrix_row, matrix_col, array):
    if 0 <= matrix_row < len(array) and 0 <= matrix_col < len(array[0]):
        return True
    return False


def take_move(old_row, old_col, new_row, new_col, array, gifts, good_kids):
    if array[new_row][new_col] == "V":
        gifts -= 1
        good_kids += 1
        array[new_row][new_col] = "S"
        array[old_row][old_col] = "-"
    elif array[new_row][new_col] == "X":
        array[new_row][new_col] = "S"
        array[old_row][old_col] = "-"
    elif array[new_row][new_col] == "C":
        array[new_row][new_col] = "S"
        array[old_row][old_col] = "-"
        array, gifts, good_kids = award_everyone(new_row, new_col, array, gifts, good_kids)
    elif array[new_row][new_col] == "-":
        array[new_row][new_col] = "S"
        array[old_row][old_col] = "-"
    position = new_row, new_col
    if gifts == 0:
        return position, array, gifts, good_kids
    return position, array, gifts, good_kids


matrix = []
santa_position = ()
nice_kids = 0
nice_kids_left = 0


count_of_presents = int(input())
neighbourhood_size = int(input())


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
    else:
        santa_position, matrix, count_of_presents, nice_kids = \
            prepare_for_action(command, santa_position, matrix, count_of_presents,nice_kids)
    if count_of_presents == 0:
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if matrix[row][col] == "V":
                    nice_kids_left += 1
        if nice_kids_left > 0:
            print("Santa ran out of presents!")
        break

print_matrix(matrix)

if nice_kids_left == 0 and count_of_presents >= 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")
  