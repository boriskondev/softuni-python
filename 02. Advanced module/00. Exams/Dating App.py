from collections import deque

matches = 0

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    elif males[-1] % 25 == 0:
        if len(males) - 2 >= 2:
            males.pop()
            males.pop()
            continue
        else:
            males.pop()
            continue
    if females[0] <= 0:
        females.popleft()
        continue
    elif females[0] % 25 == 0:
        if len(females) >= 2:
            females.popleft()
            females.popleft()
            continue
        else:
            females.popleft()
            continue
    if males and females:
        if males[-1] == females[0]:
            matches += 1
            males.pop()
            females.popleft()
        else:
            males[-1] -= 2
            females.popleft()

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in males)}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")