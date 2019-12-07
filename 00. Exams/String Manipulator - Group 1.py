string_to_process = input()

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        while char in string_to_process:
            string_to_process = string_to_process.replace(char, replacement)
        print(string_to_process)
    elif command[0] == "Includes":
        string_to_check = command[1]
        if string_to_check in string_to_process:
            print("True")
        else:
            print("False")
    elif command[0] == "Start":
        string_to_check = command[1]
        print(string_to_process.startswith(string_to_check))
    elif command[0] == "Lowercase":
        string_to_process = string_to_process.lower()
        print(string_to_process)
    elif command[0] == "FindIndex":
        char_index_to_find = command[1]
        print(string_to_process.rfind(char_index_to_find))
    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        string_to_process = string_to_process.replace(string_to_process[start_index:start_index+count], "")
        print(string_to_process)