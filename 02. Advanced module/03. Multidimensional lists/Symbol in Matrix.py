matrix_size = int(input())

matrix = []
found = False

coordinates = 0

for row in range(matrix_size):
    matrix.append([el for el in input()])

to_find = input()

for row in range(len(matrix)):
    if found:
        break
    for col in range(len(matrix)):
        if matrix[row][col] == to_find:
            coordinates = (row, col)
            found = True
            break

if found:
    print(coordinates)
else:
    print(f"{to_find} does not occur in the matrix")