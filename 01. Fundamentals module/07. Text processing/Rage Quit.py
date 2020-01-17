text = input()

current_text = ""
rage_text = ""

for i in range(len(text)):
    if text[i].isnumeric():
        multiplier = text[i]
        counter = i + 1
        while counter < len(text) and text[counter].isnumeric():
            multiplier += text[counter]
            counter += 1
        current_text = current_text.upper() * int(multiplier)
        rage_text += current_text
        current_text = ""
    else:
        current_text += text[i]

print(f"Unique symbols used: {len(set(rage_text))}")
print(rage_text)