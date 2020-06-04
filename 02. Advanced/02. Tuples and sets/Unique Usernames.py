names = int(input())

n = []

for _ in range(names):
    n.append(input())

[print(i) for i in set(n)]