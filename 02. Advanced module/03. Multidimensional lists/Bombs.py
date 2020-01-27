bomb_field = []
bombs_coordinates = []
dead_cells = []


def check_index(matrix_row, matrix_col, matrix):
    if 0 <= matrix_row < len(matrix) and 0 <= matrix_col < len(matrix[0]):
        return True
    return False


def detonate(original_coordinates, matrix):
    x = original_coordinates[0]
    y = original_coordinates[1]
    damage = matrix[x][y]
    if check_index(x-1, y-1, matrix):
        if matrix[x-1][y-1] > 0:
            matrix[x-1][y-1] -= damage
    if check_index(x-1, y, matrix):
        if matrix[x-1][y] > 0:
            matrix[x-1][y] -= damage
    if check_index(x-1, y+1, matrix):
        if matrix[x-1][y+1] > 0:
            matrix[x-1][y+1] -= damage
    if check_index(x, y+1, matrix):
        if matrix[x][y+1] > 0:
            matrix[x][y+1] -= damage
    if check_index(x+1, y+1, matrix):
        if matrix[x+1][y+1] > 0:
            matrix[x+1][y+1] -= damage
    if check_index(x+1, y, matrix):
        if matrix[x+1][y] > 0:
            matrix[x+1][y] -= damage
    if check_index(x+1, y-1, matrix):
        if matrix[x+1][y-1] > 0:
            matrix[x+1][y-1] -= damage
    if check_index(x, y-1, matrix):
        if matrix[x][y-1] > 0:
            matrix[x][y-1] -= damage
    matrix[x][y] = 0
    dead_cells.append((x, y))


field_size = int(input())

for row in range(field_size):
    bomb_field.append([int(x) for x in input().split()])

for c in input().split():
    bombs_coordinates.append([int(x) for x in c.split(",")])

for bomb_coordinate in bombs_coordinates:
    if bomb_coordinate not in dead_cells:
        detonate(bomb_coordinate, bomb_field)

alive = []

for row in range(len(bomb_field)):
    for col in range(len(bomb_field)):
        if bomb_field[row][col] > 0:
            alive.append(bomb_field[row][col])

print(dead_cells)

print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")
[print(" ".join(map(str, r))) for r in bomb_field]