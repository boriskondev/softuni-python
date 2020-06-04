input_1 = input()
input_2 = input()
text = input()

if ord(input_1) < ord(input_2):
    start = input_1
    end = input_2
else:
    start = input_2
    end = input_1

total = 0

for code in range(ord(start)+1, ord(end)):
    for char in text:
        if char == chr(code):
            total += code

print(total)