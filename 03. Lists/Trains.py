wagons_length = int(input())
wagons = [0] * wagons_length

command = input().split()

while command[0] != "End":
    if command[0] == "add":
        wagons[-1] += int(command[1])
    elif command[0] == "insert":
        index = int(command[1])
        wagons[index] += int(command[2])
    elif command[0] == "leave":
        index = int(command[1])
        wagons[index] -= int(command[2])
    command = input().split()

print(wagons)