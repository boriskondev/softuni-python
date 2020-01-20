from collections import deque

queue = deque()


while True:
    input_string = input()
    if input_string == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif input_string == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(input_string)