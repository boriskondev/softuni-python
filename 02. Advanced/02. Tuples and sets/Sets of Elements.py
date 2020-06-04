first, second = map(int, input().split())

f = []
s = []

whole = first + second

for n in range(whole):
    if n < first:
        f.append(input())
    else:
        s.append(input())

intersection = set(f) & set(s)

[print(i) for i in intersection]