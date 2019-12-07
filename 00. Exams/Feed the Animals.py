areas = {}
animals = {}

while True:
    command = input()
    if command == "Last Info":
        break
    command = command.split(":")
    if command[0] == "Add":
        animal = command[1]
        food_limit = int(command[2])
        area = command[3]
        if animal not in animals:
            animals[animal] = food_limit
        else:
            animals[animal] += food_limit
        if area not in areas:
            areas[area] = [animal]
        else:
            if animal in areas[area]:
                continue
            else:
                areas[area].append(animal)
    elif command[0] == "Feed":
        animal = command[1]
        food = int(command[2])
        area = command[3]
        if animal in animals:
            animals[animal] -= food
            if animals[animal] <= 0:
                print(f"{animal} was successfully fed")
                del animals[animal]
                areas[area].remove(animal)

sorted_animals = sorted(animals.items(), key=lambda kvp: (-kvp[1], kvp[0]))
sorted_areas = sorted(areas.items(), key=lambda kvp: len(kvp[1]), reverse=True)

print("Animals:")
[print(f"{tup[0]} -> {tup[1]}g") for tup in sorted_animals]
print("Areas with hungry animals:")
for area in sorted_areas:
    if len(area[1]) > 0:
        print(f"{area[0]} : {len(area[1])}")