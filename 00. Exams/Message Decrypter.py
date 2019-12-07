import re

pattern = r"(^\$[A-Z][a-z][a-z]+\$:\s\[\d+\]\|\[\d+\]\|\[\d+\]\|$)|(^\%[A-Z][a-z][a-z]+\%:\s\[\d+\]\|\[\d+\]\|\[\d+\]\|$)"

lines = int(input())

for line in range(lines):
    text = input()
    matches = re.findall(pattern, text)
    if not matches:
        print("Valid message not found!")
    else:
        tag, numbers = text.split(":")
        tag = tag[1:-1]
        numbers = numbers.strip().split("|")[:-1]
        decrypted_message = []
        for number in numbers:
            number = int(number[1:-1])
            decrypted_message.append(chr(number))
        print(f"{tag}: {''.join(decrypted_message)}")