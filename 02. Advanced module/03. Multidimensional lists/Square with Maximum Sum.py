matrix = []
square_matrix = []
current_sum = 0
max_sum = 0

rows, columns = map(int, input().split(", "))

for row in range(rows):
    matrix.append(list(map(int, input().split(", "))))

for row in range(rows):
    for column in range(columns):
        if row <= rows - 2 and column <= columns - 2:
            top_left = matrix[row][column]
            top_right = matrix[row][column+1]
            down_left = matrix[row+1][column]
            down_right = matrix[row+1][column+1]
            current_sum = top_left + top_right + down_left + down_right
            if max_sum < current_sum:
                max_sum = current_sum
                square_matrix = [[top_left, top_right], [down_left, down_right]]

for r in square_matrix:
    print(" ".join(map(str, r)))
print(max_sum)