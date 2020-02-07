import os

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    elif command[0] == "Create":
        file_name = command[1]
        file = open(file_name, "w")
    elif command[0] == "Add":
        file_name = command[1]
        content = command[2]
        with open(file_name, "a+") as file:
            file.write(f"{content}\n")

