def move_up(playground, player_coordinates, visited_coordinates):
    up_row = player_coordinates[0] - 1
    col = player_coordinates[1]
    if up_row >= 0:
        step_up = playground[up_row][col]
        step_up_coords = (up_row, col)
        if step_up != "#" and step_up_coords not in visited_coordinates:
            return True
        else:
            return False


def move_down(playground, player_coordinates, visited_coordinates):
    down_row = player_coordinates[0] + 1
    col = player_coordinates[1]
    if down_row <= len(playground) - 1:
        step_down = playground[down_row][col]
        step_down_coords = (down_row, col)
        if step_down != "#" and step_down_coords not in visited_coordinates:
            return True
        else:
            return False


kate_coordinates = (0, 0)
already_visited = []
moves = 0
out = False

array = [list(input()) for row in range(int(input()))]

row_count = 0
for new_row in array:
    kate_found = False
    col_count = 0
    for column in new_row:
        if column == "k":
            kate_coordinates = (row_count, col_count)
            kate_found = True
            break
        col_count += 1
    if kate_found:
        break
    row_count += 1

already_visited.append(kate_coordinates)

while True:
    if move_up(array, kate_coordinates, already_visited):
        new_row = kate_coordinates[0] - 1
        column = kate_coordinates[1]
        array[new_row + 1][column] = " "
        array[new_row][column] = "k"
        kate_coordinates = (new_row, column)
        moves += 1
        already_visited.append(kate_coordinates)
        if new_row == 0:
            moves += 1
            out = True
            break
    elif move_down(array, kate_coordinates, already_visited):
        new_row = kate_coordinates[0] + 1
        column = kate_coordinates[1]
        array[new_row - 1][column] = " "
        array[new_row][column] = "k"
        kate_coordinates = (new_row, column)
        moves += 1
        already_visited.append(kate_coordinates)
        if new_row == len(array) - 1:
            moves += 1
            out = True
            break


if out:
    print(f"Kate got out in {moves} moves")