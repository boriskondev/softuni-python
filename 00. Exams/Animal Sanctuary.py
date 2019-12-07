import re

regex = r"^n\:(?P<name>[^;]+)\;t\:(?P<kind>[^;]+)\;c\-{2}(?P<country>[a-zA-Z\s]+)$"

total_weigh = 0


for row in range(int(input())):
    text = input()
    found = re.match(regex, text)
    if found:
        name = found.group("name")
        kind = found.group("kind")
        country = found.group("country")
        weight = name + kind
        total_weigh += sum([int(x) for x in weight if x.isdigit()])
        name = ''.join([x for x in name if x.isalpha() or x == " "])
        kind = ''.join([x for x in kind if x.isalpha() or x == " "])
        print(f"{name} is a {kind} from {country}")

print(f"Total weight of animals: {total_weigh}KG")