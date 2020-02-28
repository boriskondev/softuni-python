def print_matrix(array):
    for r in array:
        print(" ".join(r))


def check_index(matrix_row, matrix_col, array):
    if 0 <= matrix_row < len(array) and 0 <= matrix_col < len(array[0]):
        return True
    return False


def ready_steady(position, what, where, how_far, matrix, enemies, destroyed_coords):
    current_row = position[0]
    current_col = position[1]
    desired_row = ""
    desired_col = ""
    if where == "up":
        desired_row = current_row - how_far
        desired_col = current_col
    elif where == "right":
        desired_row = current_row
        desired_col = current_col + how_far
    elif where == "down":
        desired_row = current_row + how_far
        desired_col = current_col
    elif where == "left":
        desired_row = current_row
        desired_col = current_col - how_far
    if check_index(desired_row, desired_col, matrix):
        if what == "move":
            if matrix[desired_row][desired_col] == ".":
                matrix[current_row][current_col] = "."
                matrix[desired_row][desired_col] = "p"
                position = desired_row, desired_col
        elif what == "shoot":
            if matrix[desired_row][desired_col] == ".":
                matrix[desired_row][desired_col] = "x"
            elif matrix[desired_row][desired_col] == "t":
                matrix[desired_row][desired_col] = "x"
                enemies += 1
            destroyed_coords.append((desired_row, desired_col))
    return position, matrix, enemies, destroyed_coords


battlefield = []
plane_position = ()
targets = 0
targets_killed = 0

destroyed_fields = []

field_size = int(input())

for row in range(field_size):
    battlefield.append(input().split())

for row in range(len(battlefield)):
    for col in range(len(battlefield)):
        if battlefield[row][col] == "p":
            plane_position = row, col
        elif battlefield[row][col] == "t":
            targets += 1

commands = int(input())

for _ in range(commands):
    action, direction, steps = input().split()
    steps = int(steps)
    plane_position, battlefield, targets_killed, destroyed_fields = \
        ready_steady(plane_position, action, direction, steps, battlefield, targets_killed, destroyed_fields)
    if targets - targets_killed == 0:
        print(f"Mission accomplished! All {targets} targets destroyed.")
        break

if targets - targets_killed > 0:
    print(f"Mission failed! {targets - targets_killed} targets left.")

print_matrix(battlefield)