weapon_parts = input().split("|")

while True:
    command = input().split()
    if command[0] == "Done":
        break
    elif command[0] == "Move":
        direction = command[1]
        index = int(command[2])
        if direction == "Left":
            if 0 <= index <= len(weapon_parts) - 1:
                if 0 <= index - 1:
                    take = weapon_parts.pop(index)
                    weapon_parts.insert(index-1, take)
        elif direction == "Right":
            if 0 <= index <= len(weapon_parts) - 1:
                if index + 1 <= len(weapon_parts) - 1:
                    take = weapon_parts.pop(index)
                    weapon_parts.insert(index+1, take)
    elif command[0] == "Check":
        what = command[1]
        if what == "Even":
            even_elements = [weapon_parts[i] for i in range(len(weapon_parts)) if i % 2 == 0]
            print(" ".join(even_elements))
        elif what == "Odd":
            odd_elements = [weapon_parts[i] for i in range(len(weapon_parts)) if i % 2 != 0]
            print(" ".join(odd_elements))


print(f"You crafted {''.join(weapon_parts)}!")