from collections import deque

matrix = []

rows, columns = [int(x) for x in input().split()]
snake = deque(input())

for row in range(1, rows + 1):
    matrix_row = []
    for col in range(columns):
        push = snake.popleft()
        matrix_row.append(push)
        snake.append(push)
    if row % 2 != 0:
        matrix.append(matrix_row)
    else:
        matrix.append(matrix_row[::-1])

[print("".join(r)) for r in matrix]