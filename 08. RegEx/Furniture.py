import re

pattern = r">>([a-zA-z ]+)<<([0-9]+\.?\d*)!(\d+)"

furniture = []
income = 0

while True:
    sentence = input()
    if sentence == "Purchase":
        break
    matches = re.findall(pattern, sentence)
    for m in matches:
        if m:
            furniture.append(m[0])
            income += float(m[1]) * int(m[2])

print("Bought furniture:")
[print(x) for x in furniture]
print(f"Total money spend: {income:.2f}")