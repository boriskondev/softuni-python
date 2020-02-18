def print_matrix(array):
    for r in array:
        print(" ".join(r))


def check_index(matrix_row, matrix_col, array):
    if 0 <= matrix_row < len(array) and 0 <= matrix_col < len(array[0]):
        return True
    return False


def check_around(r, c, array, gifts, good_kids):
    global no_more_gifts
    no_more_gifts = False
    if array[r][c] == "X":
        gifts -= 1
        array[r][c] = "-"
    elif array[r][c] == "V":
        gifts -= 1
        good_kids -= 1
        array[r][c] = "-"
    if gifts == 0:
        no_more_gifts = True
        return r, c, array, gifts, good_kids, no_more_gifts
    return r, c, array, gifts, good_kids


def award_everyone(new_row, new_col, array, gifts, good_kids):
    if check_index(new_row - 1, new_col - 1, array):
        check_around(new_row - 1, new_col - 1, array, gifts, good_kids)
        print_matrix(array)
        print()
    if check_index(new_row - 1, new_col, array):
        check_around(new_row - 1, new_col, array, gifts, good_kids)
        print_matrix(array)
        print()
    if check_index(new_row - 1, new_col + 1, array):
        check_around(new_row - 1, new_col + 1, array, gifts, good_kids)
        print_matrix(array)
        print()
    if check_index(new_row, new_col + 1, array):
        check_around(new_row, new_col + 1, array, gifts, good_kids)
        print_matrix(array)
        print()
    if check_index(new_row + 1, new_col + 1, array):
        check_around(new_row + 1, new_col + 1, array, gifts, good_kids)
        print_matrix(array)
        print()
    if check_index(new_row + 1, new_col, array):
        check_around(new_row + 1, new_col, array, gifts, good_kids)
        print_matrix(array)
        print()
    if check_index(new_row + 1, new_col - 1, array):
        check_around(new_row + 1, new_col - 1, array, gifts, good_kids)
        print_matrix(array)
        print()
    if check_index(new_row, new_col - 1, array):
        check_around(new_row, new_col - 1, array, gifts, good_kids)
        print_matrix(array)
        print()
    print_matrix(array)
    print()
    return new_row, new_col, array, gifts, good_kids


def take_move(old_row, old_col, new_row, new_col, array, gifts, good_kids):
    if array[new_row][new_col] == "V":
        gifts -= 1
        good_kids -= 1
        array[new_row][new_col] = "S"
        array[old_row][old_col] = "-"
    elif array[new_row][new_col] == "X":
        array[new_row][new_col] = "S"
        array[old_row][old_col] = "-"
    elif array[new_row][new_col] == "C":
        array[new_row][new_col] = "S"
        array[old_row][old_col] = "-"
        award_everyone(new_row, new_col, array, gifts, good_kids)
    elif array[new_row][new_col] == "-":
        array[new_row][new_col] = "S"
        array[old_row][old_col] = "-"
    print_matrix(array)
    position = new_row, new_col
    return position, array, gifts, good_kids


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


matrix = []
santa_position = ()
nice_kids = 0
nice_kids_left = 0
no_more_gifts = False


count_of_presents = int(input())
neighbourhood_size = int(input())


for _ in range(neighbourhood_size):
    matrix.append(input().split())

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "S":
            santa_position = row, col
        if matrix[row][col] == "V":
            nice_kids += 1

while True:
    print(count_of_presents)
    command = input()
    if command == "Christmas morning":
        break
    else:
        santa_position, matrix, count_of_presents, nice_kids = \
            prepare_for_action(command, santa_position, matrix, count_of_presents,nice_kids)
    if count_of_presents == 0:
        print("Santa ran out of presents!")
        break

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "V":
            nice_kids_left += 1

print_matrix(matrix)

if nice_kids_left == 0 and count_of_presents >= 0:
    print(f"Good job, Santa! {nice_kids_left} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")
