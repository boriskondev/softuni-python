import os

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    elif command[0] == "Create":
        file_name = command[1]
        file = open(file_name, "w")
    elif command[0] == "Add":
        file_name, content = command[1], command[2]
        with open(file_name, "a+") as file:
            file.write(f"{content}\n")
    elif command[0] == "Replace":
        file_name, old_string, new_string = command[1], command[2], command[3]
        if os.path.exists(file_name):
            with open(file_name, "rt", encoding="utf8") as file:
                data = file.read()
                data = data.replace(old_string, new_string)
            with open(file_name, "wt", encoding="utf8") as file:
                file.write(data)
        else:
            print("An error occurred")
    elif command[0] == "Delete":
        file_name = command[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")