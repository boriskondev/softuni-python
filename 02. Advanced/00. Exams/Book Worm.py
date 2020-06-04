def check_index(matrix_row, matrix_col, array):
    if 0 <= matrix_row < len(array) and 0 <= matrix_col < len(array[0]):
        return True
    return False


def move_up(position, array, string):
    player_row, player_col = position[0], position[1]
    if check_index(player_row - 1, player_col, array):
        if array[player_row - 1][player_col] != "-":
            string += array[player_row - 1][player_col]
        array[player_row - 1][player_col] = "P"
        position = player_row - 1, player_col
        array[player_row][player_col] = "-"
    else:
        if len(string) > 0:
            string = string[:-1]
    return position, array, string


def move_down(position, array, string):
    player_row, player_col = position[0], position[1]
    if check_index(player_row + 1, player_col, array):
        if array[player_row + 1][player_col] != "-":
            string += array[player_row + 1][player_col]
        array[player_row + 1][player_col] = "P"
        position = player_row + 1, player_col
        array[player_row][player_col] = "-"
    else:
        if len(string) > 0:
            string = string[:-1]
    return position, array, string


def move_left(position, array, string):
    player_row, player_col = position[0], position[1]
    if check_index(player_row, player_col - 1, array):
        if array[player_row][player_col - 1] != "-":
            string += array[player_row][player_col - 1]
        array[player_row][player_col - 1] = "P"
        position = player_row, player_col - 1
        array[player_row][player_col] = "-"
    else:
        if len(string) > 0:
            string = string[:-1]
    return position, array, string


def move_right(position, array, string):
    player_row, player_col = position[0], position[1]
    if check_index(player_row, player_col + 1, array):
        if array[player_row][player_col + 1] != "-":
            string += array[player_row][player_col + 1]
        array[player_row][player_col + 1] = "P"
        position = player_row, player_col + 1
        array[player_row][player_col] = "-"
    else:
        if len(string) > 0:
            string = string[:-1]
    return position, array, string


def print_matrix(mtr):
    for r in mtr:
        print("".join(map(str, r)))


matrix = []
player_coordinates = 0

initial_string = input()
matrix_size = int(input())

for row in range(matrix_size):
    data = [x for x in input()]
    for column in range(len(data)):
        if data[column] == "P":
            player_coordinates = row, column
    matrix.append(data)

commands = int(input())

for _ in range(commands):
    command = input()
    if command == "up":
        player_coordinates, matrix, initial_string = move_up(player_coordinates, matrix, initial_string)
    elif command == "down":
        player_coordinates, matrix, initial_string = move_down(player_coordinates, matrix, initial_string)
    elif command == "left":
        player_coordinates, matrix, initial_string = move_left(player_coordinates, matrix, initial_string)
    elif command == "right":
        player_coordinates, matrix, initial_string = move_right(player_coordinates, matrix, initial_string)

print(initial_string)
print_matrix(matrix)