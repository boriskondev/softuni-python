multiplier = int(input())
multiplied = [int(x) * multiplier for x in input().split()]
print(" ".join(list(map(str, multiplied))))