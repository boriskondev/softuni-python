import re

pattern = r"^[A-Z][a-z' ]+:[A-Z ]+$"

text = input()

while text != "end":
    encrypted_string = ""
    matches = re.findall(pattern, text)
    if not matches:
        print("Invalid input!")
    else:
        for m in matches:
            artist, song = m.split(":")
            key = len(artist)
            for char in m:
                if char == ":":
                    encrypted_string += "@"
                elif char == " " or char == "'":
                    encrypted_string += char
                elif char.isupper():
                    if ord(char) + key > 90:
                        start_from = (ord(char) + key) - 90
                        encrypted_string += chr(64 + start_from)
                    else:
                        encrypted_string += chr(ord(char) + key)
                elif char.islower():
                    if ord(char) + key > 122:
                        start_from = (ord(char) + key) - 122
                        encrypted_string += chr(96 + start_from)
                    else:
                        encrypted_string += chr(ord(char) + key)
            print(f"Successful encryption: {encrypted_string}")
    text = input()