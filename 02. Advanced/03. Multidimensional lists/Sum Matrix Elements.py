matrix = []
sum_matrix = 0

rows, columns = map(int, input().split(", "))

for row in range(rows):
    matrix.append(list(map(int, input().split(", "))))

for row in matrix:
    sum_matrix += sum(row)


print(sum_matrix)
print(matrix)