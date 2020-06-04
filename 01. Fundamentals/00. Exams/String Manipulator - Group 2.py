processed_string = input()

while True:
    command = input().split()
    if command[0] == "Done":
        break
    elif command[0] == "Change":
        char = command[1]
        replacement = command[2]
        while char in processed_string:
            processed_string = processed_string.replace(char, replacement)
        print(processed_string)
    elif command[0] == "Includes":
        is_included = command[1]
        if is_included in processed_string:
            print("True")
        else:
            print("False")
    elif command[0] == "End":
        ends_with = command[1]
        if processed_string.endswith(ends_with):
            print("True")
        else:
            print("False")
    elif command[0] == "Uppercase":
        processed_string = processed_string.upper()
        print(processed_string)
    elif command[0] == "FindIndex":
        what_to_search = command[1]
        searched_index = processed_string.find(what_to_search)
        print(searched_index)
    elif command[0] == "Cut":
        start = int(command[1])
        length = int(command[2])
        processed_string = processed_string[start:start+length]
        print(processed_string)