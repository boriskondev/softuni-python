text = input()

encrypted_message = ""

for char in text:
    encrypted_message += chr(ord(char) + 3)

print(encrypted_message)