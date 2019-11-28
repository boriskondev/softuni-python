import re

pattern = r" ([A-Za-z0-9]+[-._]*[A-Za-z0-9]*\@[A-Za-z]+\-?[A-Za-z]+(\.[a-z]+)+)"

text = input()

matches = re.findall(pattern, text)

for match in matches:
    print(match[0])