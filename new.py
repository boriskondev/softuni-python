import re

counter = 0

text = input()

while counter < len(text):
    for t in text[counter:]:
        counter += 1
        pattern = t + '{2,}'
        string = re.sub(pattern, t, text)
        text = string
        break

print(text)