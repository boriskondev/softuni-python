store = {}

while True:
    command = input()
    if command == "END":
        break
    command = command.split("->")
    if command[0] == "Add":
        if command[1] not in store:
            store[command[1]] = command[2].split(",")
        else:
            store[command[1]].extend(command[2].split(","))
    elif command[0] == "Remove":
        if command[1] in store:
            del store[command[1]]
        else:
            continue

sorted_stores = sorted(store.items(), key=lambda kvp: (len(kvp[1]), kvp[0]), reverse=True)

print("Stores list:")
for store in sorted_stores:
    print(store[0])
    [print(f"<<{x}>>") for x in store[1]]