from collections import deque

initial_queue = deque(reversed(input().split()))

current_queue = deque()

result = 0

while initial_queue:
    last_item = initial_queue[-1]
    if initial_queue[-1].isalnum():
        current_queue.append(int(last_item))
        initial_queue.pop()
    else:
        if len(current_queue) > 1:
            result = current_queue.popleft()
            initial_queue.pop()
            if last_item == "+":
                while current_queue:
                    result += current_queue.popleft()
            elif last_item == "-":
                while current_queue:
                    result -= current_queue.popleft()
            elif last_item == "*":
                while current_queue:
                    result *= current_queue.popleft()
            elif last_item == "/":
                while current_queue:
                    result //= current_queue.popleft()
            current_queue.insert(0, result)

print(current_queue[0])