name = input()

while True:
    command = input().split()
    if command[0] == "Sign" and command[1] == "up":
        break
    elif command[0] == "Case":
        case_type = command[1]
        if case_type == "lower":
            name = name.lower()
        elif case_type == "upper":
            name = name.upper()
        print(name)
    elif command[0] == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(name) - 1 and 0 <= end_index <= len(name) - 1:
            print(name[start_index:end_index+1][::-1])
    elif command[0] == "Cut":
        part_to_cut = command[1]
        if part_to_cut in name:
            name = name.replace(part_to_cut, "")
            print(name)
        else:
            print(f"The word {name} doesn't contain {part_to_cut}.")
    elif command[0] == "Replace":
        char = command[1]
        if char in name:
            while char in name:
                name = name.replace(char, "*")
        print(name)
    elif command[0] == "Check":
        char = command[1]
        if char in name:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
