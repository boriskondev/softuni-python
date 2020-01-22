initial_values = list(map(float, input().split()))

values = {}

for v in initial_values:
    if v in values:
        values[v] += 1
    else:
        values[v] = 1

[print(f"{kvp[0]} - {kvp[1]} times") for kvp in values.items()]