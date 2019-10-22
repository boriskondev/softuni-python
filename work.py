def move_up(playground, player_coordinates, visited_coordinates):
    up_row = player_coordinates[0] - 1
    col = player_coordinates[1]
    if up_row >= 0:
        step_up = playground[up_row][col]
        if step_up != "#" and step_up not in visited_coordinates:
            return True
        else:
            return False


def move_down(playground, player_coordinates, visited_coordinates):
    down_row = player_coordinates[0] + 1
    col = player_coordinates[1]
    if down_row <= len(playground) - 1:
        step_down = playground[down_row][col]
        if step_down != "#" and step_down not in visited_coordinates:
            return True
        else:
            return False


kate_coordinates = (0, 0)
already_visited = []
moves = 0
out = False

array = [list(input()) for row in range(int(input()))]

row_count = 0
for row in array:
    kate_found = False
    col_count = 0
    for column in row:
        if column == "k":
            kate_coordinates = (row_count, col_count)
            kate_found = True
            break
        col_count += 1
    if kate_found:
        break
    row_count += 1


while True:
    if move_up(array, kate_coordinates, already_visited):
        row = kate_coordinates[0]
        column = kate_coordinates[1]
        array[row][column] = " "
        array[row-1][column] = "k"
        kate_coordinates = (row-1, column)
        moves += 1
        already_visited.append(kate_coordinates)
        if row - 1 == 0:
            moves += 1
            out = True
            break
        continue
    elif move_down(array, kate_coordinates, already_visited):
        pass

if out:
    print(f"Kate got out in {moves} moves")