matrix = []
square_matrix = []
current_sum = 0
max_sum = 0

rows, columns = map(int, input().split())

for row in range(rows):
    matrix.append(list(map(int, input().split())))

for row in range(rows - 2):
    for column in range(columns - 2):
        top_left = matrix[row][column]
        top_middle = matrix[row][column + 1]
        top_right = matrix[row][column + 2]
        top_sum = top_left + top_middle + top_right
        middle_left = matrix[row + 1][column]
        middle_middle = matrix[row + 1][column + 1]
        middle_right = matrix[row + 1][column + 2]
        middle_sum = middle_left + middle_middle + middle_right
        down_left = matrix[row + 2][column]
        down_middle = matrix[row + 2][column + 1]
        down_right = matrix[row + 2][column + 2]
        down_sum = down_left + down_middle + down_right
        current_sum = top_sum + middle_sum + down_sum
        if current_sum > max_sum:
            max_sum = current_sum
            square_matrix = [[top_left, top_middle, top_right],
                             [middle_left, middle_middle, middle_right],
                             [down_left, down_middle, down_right],]

print(f"Sum = {max_sum}")
for r in square_matrix:
    print(" ".join(map(str, r)))