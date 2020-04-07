from collections import deque

elements_to_enqueue, elements_to_dequeue, to_look_for = map(int, input().split())

queue = deque(map(int, input().split()))

for n in range(elements_to_dequeue):
    queue.popleft()

if queue:
    if to_look_for in queue:
        print("True")
    else:
        print(min(queue))
else:
    print("0")