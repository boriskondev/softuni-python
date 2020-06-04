usernames = input().split(", ")

counter = 0

for username in usernames:
    if 3 <= len(username) <= 16:
        for symbol in username:
            if symbol.isalnum():
                counter += 1
            elif symbol == "-":
                counter += 1
            elif symbol == "_":
                counter += 1
        if counter == len(username):
            print(username)
            counter = 0
        counter = 0