from collections import deque

queue = deque()

water_quantity = int(input())

name = input()

while name != "Start":
    queue.append(name)
    name = input()

while True:
    command = input()
    if command == "End":
        print(f"{water_quantity} liters left")
        break
    elif command.split()[0] == "refill":
        water_quantity += int(command.split()[1])
    else:
        water_wanted = int(command)
        if water_quantity >= int(command):
            print(f"{queue.popleft()} got water")
            water_quantity -= int(command)
        else:
            print(f"{queue.popleft()} must wait")


