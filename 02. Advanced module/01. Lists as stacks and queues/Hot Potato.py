from collections import deque

counter = 0

queue = deque()

[queue.append(name) for name in input().split()]
hot_potato = int(input())

while queue:
    counter += 1
    if counter % hot_potato == 0:
        queue.popleft()
    else:
        pass