capacity = int(input())

usernames = {}

while True:
    command = input().split("=")
    if command[0] == "Statistics":
        break
    elif command[0] == "Add":
        name = command[1]
        sent = int(command[2])
        received = int(command[3])
        if name not in usernames:
            usernames[name] = [sent, received]
    elif command[0] == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in usernames and receiver in usernames:
            usernames[sender][0] += 1
            if sum(usernames[sender]) >= capacity:
                print(f"{sender} reached the capacity!")
                del usernames[sender]
            usernames[receiver][1] += 1
            if sum(usernames[receiver]) >= capacity:
                print(f"{receiver} reached the capacity!")
                del usernames[receiver]
    elif command[0] == "Empty":
        what_or_who = command[1]
        if what_or_who == "All":
            usernames.clear()
        else:
            if what_or_who in usernames:
                del usernames[what_or_who]

print(f"Users count: {len(usernames.keys())}")
for user, messages in sorted(usernames.items(), key=lambda x: (-x[1][1], x[0])):
    print(f"{user} - {sum(messages)}")