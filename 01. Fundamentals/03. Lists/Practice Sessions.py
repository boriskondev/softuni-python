roads = {}

while True:
    command = input()
    if command == "END":
        break
    command = command.split("->")
    if command[0] == "Add":
        current_road = command[1]
        current_racer = command[2]
        if current_road not in roads:
            roads[current_road] = [current_racer]
        else:
            roads[current_road].append(current_racer)
    elif command[0] == "Move":
        current_road = command[1]
        current_racer = command[2]
        next_road = command[3]
        if current_racer in roads[current_road]:
            roads[current_road].remove(current_racer)
            roads[next_road].append(current_racer)
    elif command[0] == "Close":
        current_road = command[1]
        if current_road in roads:
            del roads[current_road]

print("Practice sessions:")

sorted_roads = sorted(roads.items(), key=lambda k: (-len(k[1]), k[0]))

for road in sorted_roads:
    print(road[0])
    [print(f"++{x}") for x in road[1]]
