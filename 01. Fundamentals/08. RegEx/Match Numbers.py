import re

text = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, text)

print(" ".join([text[match.start():match.end()] for match in matches]))