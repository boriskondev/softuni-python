energy = 100
coins = 100

bankrupt = False

working_day_events = input().split("|")

for event_or_item in working_day_events:
    event_item, value = event_or_item.split("-")
    value = int(value)
    if event_item == "rest":
        if energy + value > 100:
            value = 100 - energy
            energy += value
        else:
            energy += value
        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif event_item == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - value > 0:
            coins -= value
            print(f"You bought {event_item}.")
        else:
            print(f"Closed! Cannot afford {event_item}.")
            bankrupt = True
            break

if not bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")