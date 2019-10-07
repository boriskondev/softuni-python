key = int(input())
lines = int(input())

message = ""

for line in range(1, lines+1):
    char = input()
    message += (chr(ord(char) + key))

print(message)