def check_index(matrix_row, matrix_col, array):
    if 0 <= matrix_row < len(array) and 0 <= matrix_col < len(array):
        return True
    return False


matrix = []
best_result = 0
best_direction = ""
best_move_coords = []

field_size = int(input())

for _ in range(field_size):
    matrix.append(input().split(" "))

bunny_position = 0

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "B":
            bunny_position = row, col

original_position = bunny_position

cannot_move = False
bunny_position = original_position
current_result = 0
current_move_coords = []

# UP
while True:
    if cannot_move:
        break
    current_row, current_col = bunny_position[0], bunny_position[1]
    desired_row = current_row - 1
    desired_col = current_col
    if check_index(desired_row, desired_col, matrix):
        if matrix[desired_row][desired_col] != "X":
            current_result += int(matrix[desired_row][desired_col])
            current_move_coords.append([current_row, current_col])
            bunny_position = desired_row, desired_col
        else:
            current_move_coords.append([current_row, current_col])
            cannot_move = True
            break
    else:
        current_move_coords.append([current_row, current_col])
        cannot_move = True
        break

if current_result > best_result:
    best_result = current_result
    best_move_coords = current_move_coords
    best_direction = "up"

cannot_move = False
bunny_position = original_position
current_result = 0
current_move_coords = []

# DOWN
while True:
    if cannot_move:
        break
    current_row, current_col = bunny_position[0], bunny_position[1]
    desired_row = current_row + 1
    desired_col = current_col
    if check_index(desired_row, desired_col, matrix):
        if matrix[desired_row][desired_col] != "X":
            current_result += int(matrix[desired_row][desired_col])
            current_move_coords.append([current_row, current_col])
            bunny_position = desired_row, desired_col
        else:
            current_move_coords.append([current_row, current_col])
            cannot_move = True
            break
    else:
        current_move_coords.append([current_row, current_col])
        cannot_move = True
        break

if current_result > best_result:
    best_result = current_result
    best_move_coords = current_move_coords
    best_direction = "down"

cannot_move = False
bunny_position = original_position
current_result = 0
current_move_coords = []

# LEFT
while True:
    if cannot_move:
        break
    current_row, current_col = bunny_position[0], bunny_position[1]
    desired_row = current_row
    desired_col = current_col - 1
    if check_index(desired_row, desired_col, matrix):
        if matrix[desired_row][desired_col] != "X":
            current_result += int(matrix[desired_row][desired_col])
            current_move_coords.append([current_row, current_col])
            bunny_position = desired_row, desired_col
        else:
            current_move_coords.append([current_row, current_col])
            cannot_move = True
            break
    else:
        current_move_coords.append([current_row, current_col])
        cannot_move = True
        break

if current_result > best_result:
    best_result = current_result
    best_move_coords = current_move_coords
    best_direction = "left"

cannot_move = False
bunny_position = original_position
current_result = 0
current_move_coords = []

# RIGHT
while True:
    if cannot_move:
        break
    current_row, current_col = bunny_position[0], bunny_position[1]
    desired_row = current_row
    desired_col = current_col + 1
    if check_index(desired_row, desired_col, matrix):
        if matrix[desired_row][desired_col] != "X":
            current_result += int(matrix[desired_row][desired_col])
            current_move_coords.append([current_row, current_col])
            bunny_position = desired_row, desired_col
        else:
            current_move_coords.append([current_row, current_col])
            cannot_move = True
            break
    else:
        current_move_coords.append([current_row, current_col])
        cannot_move = True
        break

if current_result > best_result:
    best_result = current_result
    best_move_coords = current_move_coords
    best_direction = "right"

cannot_move = False
bunny_position = original_position
current_result = 0
current_move_coords = []

print(best_direction)
for coords in best_move_coords[1:]:
    print(coords)
print(best_result)

