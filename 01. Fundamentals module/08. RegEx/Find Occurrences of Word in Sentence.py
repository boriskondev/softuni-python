import re

sentence = input().lower()
word = input().lower()

pattern = f"\\b{word}\\b"

matches = re.findall(pattern, sentence)

print(len(matches))