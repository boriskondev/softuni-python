heroes = {name: {} for name in input().split(", ")}

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    name, item, cost = command
    if name not in heroes:
        heroes[name] = {}
        if item not in heroes[name]:
            heroes[name][item] = int(cost)
    else:
        if item not in heroes[name]:
            heroes[name][item] = int(cost)

[print(f"{hero} -> Items: {len(heroes[hero])}, Cost: {sum(heroes[hero].values())}") for hero in heroes]
