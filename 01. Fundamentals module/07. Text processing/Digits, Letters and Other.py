input_string = input()

digits = ""
letters = ""
others = ""

for char in input_string:
    if char.isnumeric():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(digits)
print(letters)
print(others)