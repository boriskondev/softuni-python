import re

pattern = r"^(?P<around_user>U\$)(?P<username>[A-Z][a-z][a-z]+)(?P=around_user)(?P<around_pass>P@\$)(?P<pass>[a-z][a-z][a-z][a-z][a-z]+\d+)(?P=around_pass)$"

successful_regs = 0

lines = int(input())

for line in range(lines):
    registration = input()
    match = re.match(pattern, registration)
    if not match:
        print("Invalid username or password")
    else:
        username = match.group("username")
        password = match.group("pass")
        print("Registration was successful")
        print(f"Username: {username}, Password: {password}")
        successful_regs += 1

print(f"Successful registrations: {successful_regs}")


