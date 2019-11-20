lines = int(input())

name_start = 0
name_end = 0
age_start = 0
age_end = 0

for line in range(lines):
    text = input()
    for i in range(len(text)):
        if text[i] == "@":
            name_start = i
        elif text[i] == "|":
            name_end = i
        elif text[i] == "#":
            age_start = i
        elif text[i] == "*":
            age_end = i
    if name_start < name_end and age_start < age_end:
        name = text[name_start+1:name_end]
        age = int(text[age_start+1:age_end])
        print(f"{name} is {age} years old.")