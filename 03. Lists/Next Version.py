current = list(map(int, input().split(".")))

if current[2] == 9:
    current[2] = 0
    if current[1] < 9:
        current[1] += 1
    else:
        current[1] = 0
        current[0] += 1
else:
    current[2] += 1

current = list(map(str, current))

print(".".join(current))