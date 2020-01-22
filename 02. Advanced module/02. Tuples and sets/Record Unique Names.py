people = []

for _ in range(int(input())):
    people.append(input())

[print(p) for p in set(people)]