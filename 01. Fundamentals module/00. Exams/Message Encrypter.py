import re

pattern = r"\*[A-Z][a-z][a-z]+\*\:\s\[[A-Za-z]\]\|\[[A-Za-z]\]\|\[[A-Za-z]\]\|$|\@[A-Z][a-z][a-z]+\@\:\s\[[A-Za-z]\]\|\[[A-Za-z]\]\|\[[A-Za-z]\]\|$"

rows = int(input())

for line in range(rows):
    text = input()
    matches = re.findall(pattern, text)
    if not matches:
        print("Valid message not found!")
    else:
        for match in matches:
            tag, numbers = match.split(":")
            tag = tag[1:-1]
            numbers = numbers.strip().split("|")[:-1]
            decrypted_message = []
            for number in numbers:
                number = number[1:-1]
                decrypted_message.append(str(ord(number)))
            print(f"{tag}: {' '.join(decrypted_message)}")