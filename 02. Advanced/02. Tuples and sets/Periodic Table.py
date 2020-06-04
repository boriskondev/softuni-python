rows = int(input())

elements = []

for row in range(rows):
    elements += input().split()

[print(el) for el in set(elements)]