resources = {}

while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())
    resource = command
    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for res in resources:
    print(f"{res} -> {resources[res]}")