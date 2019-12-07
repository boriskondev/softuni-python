usernames = {}

while True:
    command = input().split("->")
    if command[0] == "Statistics":
        break
    elif command[0] == "Add":
        user_to_add = command[1]
        if user_to_add not in usernames:
            usernames[user_to_add] = []
        else:
            print(f"{user_to_add} is already registered")
    elif command[0] == "Send":
        user_to_send = command[1]
        email = command[2]
        if user_to_send in usernames:
            usernames[user_to_send].append(email)
    elif command[0] == "Delete":
        user_to_delete = command[1]
        if user_to_delete in usernames:
            del usernames[user_to_delete]
        else:
            print(f"{user_to_delete} not found!")

print(f"Users count: {len(usernames.keys())}")

for user, emails in sorted(usernames.items(), key=lambda x: (-len(x[1]), x[0])):
    print(user)
    [print(f"- {x}") for x in emails]