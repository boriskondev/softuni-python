matrix = []

for _ in range(int(input())):
    matrix.append(input().split(" "))

bunny_position = 0

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "B":
            bunny_position = row, col

original_position = bunny_position

best_result = 0
best_direction = ""
best_move_coords = []
cannot_move = 0

directions = ["up", "right", "down", "left"]

for direction in directions:
    cannot_move = False
    bunny_position = original_position
    current_result = 0
    current_move_coords = []
    while True:
        if cannot_move:
            break
        current_row, current_col = bunny_position[0], bunny_position[1]
        if direction == "up":
            desired_row, desired_col = current_row - 1, current_col
        elif direction == "right":
            desired_row, desired_col = current_row, current_col + 1
        elif direction == "down":
            desired_row, desired_col = current_row + 1, current_col
        else:
            desired_row, desired_col = current_row, current_col - 1
        if 0 <= desired_row < len(matrix) and 0 <= desired_col < len(matrix):
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
            best_direction = direction


print(best_direction)
for coords in best_move_coords[1:]:
    print(coords)
print(best_result)