text = input()

total_strength = 0

new_text = []

for i in range(len(text)):
    if total_strength > 0 and text[i] != ">":
        total_strength -= 1
        continue
    if i < len(text):
        if text[i] == ">":
            total_strength += int(text[i + 1])
            new_text.append(text[i])
        else:
            new_text.append(text[i])

print(''.join(new_text))