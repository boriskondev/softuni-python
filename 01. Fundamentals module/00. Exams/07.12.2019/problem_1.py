email = input()

while True:
    command = input().split()
    if command[0] == "Complete":
        break
    elif command[0] == "Make":
        casing = command[1]
        if casing == "Upper":
            email = email.upper()
            print(email)
        elif casing == "Lower":
            email = email.lower()
            print(email)
    elif command[0] == "GetDomain":
        count = int(command[1])
        if 0 <= count <= len(email) - 1:
            print_up_to = len(email) - count
            print(email[print_up_to:])
    elif command[0] == "GetUsername":
        if "@" in email:
            monkey_index = email.index("@")
            print(email[:monkey_index])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif command[0] == "Replace":
        char = command[1]
        while char in email:
            email = email.replace(char, "-")
        print(email)
    elif command[0] == "Encrypt":
        encrypted = [str(ord(x)) for x in email]
        print(" ".join(encrypted))