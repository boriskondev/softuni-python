array = []
kate_coordinates = ""
already_visited = []


def up(array, coordinates, already_been): #number of moves to be added
    row = coordinates[0] - 1
    column = coordinates[1]
    step_up = array[row][column]
    if step_up != "#" and step_up not in already_been:
        array[coordinates[0]][coordinates[1]] = " "
        array[row][column] = "k"
        coordinates = (row, column)
        already_been.append(coordinates)
        return array, coordinates, already_been
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

print(array)

try_up = up(array, kate_coordinates, already_visited)
if try_up:
    kate_coordinates = try_up

print(array)