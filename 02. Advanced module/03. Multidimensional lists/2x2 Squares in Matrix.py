matrix = []
square_matrix = []
equal_squares = 0

rows, columns = map(int, input().split())

for row in range(rows):
    matrix.append(input().split())

for row in range(rows - 1):
    for column in range(columns - 1):
        top_left = matrix[row][column]
        top_right = matrix[row][column+1]
        down_left = matrix[row+1][column]
        down_right = matrix[row+1][column+1]
        if top_left == top_right == down_left == down_right:
            equal_squares += 1

print(equal_squares)