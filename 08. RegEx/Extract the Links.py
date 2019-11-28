import re

pattern = r"(w{3}\.[A-Za-z0-9\-]+(\.[a-z]+)+)"

while True:
    text = input()
    if not text:
        break
    matches = re.findall(pattern, text)
    for m in matches:
        print(m[0])
