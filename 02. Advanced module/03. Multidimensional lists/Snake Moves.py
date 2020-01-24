from collections import deque

matrix = []

rows, columns = [int(x) for x in input().split()]
snake = deque(list(input()))

for row in range(rows):
    matrix_row = []
    for col in range(columns):
        push = snake.popleft()
        matrix_row.append(push)
        snake.append(push)
    matrix.append(matrix_row)

for r in matrix:
    print("".join(r))