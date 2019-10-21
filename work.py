array = []
kate_coordinates = ""
already_visited = []


def up(array, coordinates, already_been, moves, game_exit):
    r = coordinates[0] - 1
    c = coordinates[1]
    if r > 0:
        step_up = array[r][c]
        if step_up != "#" and step_up not in already_been:
            array[r][c] = "k"
            array[coordinates[0]][coordinates[1]] = " "
            coordinates = (r, c)
            already_been.append(coordinates)
            moves += 1
            return array, coordinates, already_been, moves, game_exit
    elif r == 0:
        game_exit = True
        moves += 1
        return array, coordinates, already_been, moves, game_exit
    else:
        return False


rows = int(input())

for row in range(rows):
    array.append(list(input()))

row_count = 0

for row in array:
    col_count = 0
    for col in row:
        if col == "k":
            kate_coordinates = (row_count, col_count)
        col_count += 1
    row_count += 1

moves = 0

try_up = up(array, kate_coordinates, already_visited, moves)
if try_up:
    kate_coordinates = try_up
