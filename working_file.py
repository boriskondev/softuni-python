array = []
kate_coordinates = ""
already_visited = []

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

print(len(array))







'''
def move_up(playground, player_coordinates, visited_coordinates):
    up_row = player_coordinates[0] - 1
    column = player_coordinates[1]
    if up_row >= 0:
        step_up = playground[up_row][column]
        if step_up != "#" and step_up not in visited_coordinates:
            playground[up_row][column] = "k"
            playground[player_coordinates[0]][player_coordinates[1]] = " "
            player_coordinates = (up_row, column)
            visited_coordinates.append(player_coordinates)

            return playground, player_coordinates, visited_coordinates
    elif up_row == 0:
        game_exit = True
        return playground, player_coordinates, visited_coordinates
    else:
        return False
'''
