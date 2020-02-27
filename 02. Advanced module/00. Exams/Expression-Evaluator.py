from collections import deque

initial_queue = deque(reversed(input().split()))

current_queue = deque()

result = 0

while initial_queue:
    last_item = initial_queue[-1]
    if last_item.isdigit():
        last_item = int(last_item)
        current_queue.append(last_item)
        initial_queue.pop()
    elif last_item[0] == "-" and len(last_item) > 1:
        last_item = int(last_item[1]) * -1
        current_queue.append(last_item)
        initial_queue.pop()
    else:
        result = current_queue.popleft()
        if len(current_queue) >= 1:
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
            initial_queue.pop()
            current_queue.insert(0, result)
        else:
            break

print(current_queue[0])