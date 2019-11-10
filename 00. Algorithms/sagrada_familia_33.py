import itertools
numbers = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]
result = []

for i in range(0, len(numbers)+1):
    for seq in itertools.combinations(numbers, i):
        if sum(seq) == 33:
            result.append(seq)

print(f"Possible combinations: {len(result)}")

for i in range(2, len(numbers)+1):
    combinatitons_count = len([x for x in result if len(x) == i])
    if combinatitons_count != 0:
        print(f"Combinations of {i} numbers: ", end=" ")
        print(combinatitons_count)