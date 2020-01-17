gifts_to_buy = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    command = command.split()
    if command[0] == "OutOfStock":
        item = command[1]
        for gift_bought in gifts_to_buy:
            if gift_bought == item:
                index = gifts_to_buy.index(item)
                gifts_to_buy.pop(index)
                gifts_to_buy.insert(index, "None")
    elif command[0] == "Required":
        index = int(command[2])
        if 0 <= index <= len(gifts_to_buy):
            gifts_to_buy[index] = command[1]
        else:
            continue
    elif command[0] == "JustInCase":
        gifts_to_buy[-1] = command[1]

gifts_to_buy = list(filter(lambda x: x != "None", gifts_to_buy))

print(" ".join(gifts_to_buy))