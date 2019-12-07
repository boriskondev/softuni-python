import re

pattern = r"^(?P<start_end>.+)>(?P<numbers>\d{3})\|(?P<lower_letters>[a-z]{3})\|(?P<upper_letters>[A-Z]{3})\|(?P<symbols>[^<>]{3})<(?P=start_end)$"

rows = int(input())

for row in range(rows):
    text = input()
    match = re.match(pattern, text)
    if not match:
        print("Try another password!")
    else:
        numbers = match.group("numbers")
        lower = match.group("lower_letters")
        upper = match.group("upper_letters")
        symbols = match.group("symbols")
        print(f"Password: {numbers}{lower}{upper}{symbols}")