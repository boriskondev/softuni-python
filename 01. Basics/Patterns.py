n = int(input())

for row in range(1, n+1):
    for col in range(row):
        print("*", end="")
    print()
for row in range(n-1, 0, -1):
    for col in range(row):
        print("*", end="")
    print()