matrix = []

for row in range(int(input())):
    matrix.append([int(x) for x in input().split(", ")])

first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[(len(matrix)-1-i)][i] for i in range(len(matrix)-1, -1, -1)]

print(f"First diagonal: {', '.join(list(map(str, first_diagonal)))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(list(map(str, second_diagonal)))}. Sum: {sum(second_diagonal)}")
