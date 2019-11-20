texts_list = input().split()

result = 0

for text in texts_list:
    start_letter = text[0]
    number = int(text[1:-1])
    end_letter = text[-1]
    if start_letter.isupper():
        number /= (ord(start_letter.upper()) - 64)
    elif start_letter.islower():
        number *= (ord(start_letter.upper()) - 64)
    if end_letter.isupper():
        number -= (ord(end_letter.upper()) - 64)
    elif end_letter.islower():
        number += (ord(end_letter.upper()) - 64)
    result += number

print(f"{result:.2f}")