text = input()

filtered_text = []

for i in range(len(text)):
    if i < len(text) - 1:
        if text[i] == text[i + 1]:
            continue
        else:
            filtered_text.append(text[i])
    else:
        filtered_text.append(text[i])

print("".join(filtered_text))