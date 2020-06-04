initial = input().split()

print(sum([round(float(x)) * len(initial) for x in initial]))
