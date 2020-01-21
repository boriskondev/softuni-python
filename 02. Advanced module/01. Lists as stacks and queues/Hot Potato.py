from collections import deque

counter = 0

queue = deque()

[queue.append(name) for name in input().split()]
hot_potato = int(input())

while queue:
    if len(queue) == 1:
        break
    counter += 1
    if counter % hot_potato == 0:
        print(f"Removed {queue.popleft()}")
    else:
        person = queue.popleft()
        queue.append(person)

print(f"Last is {queue.popleft()}")