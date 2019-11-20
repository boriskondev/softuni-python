string_one, string_two = input_string = input().split()

total = 0

for i in range(max(len(string_one), len(string_two))):
    if i < len(string_one) and i < len(string_two):
        total += ord(string_one[i]) * ord(string_two[i])
    else:
        if i < len(string_one):
            total += ord(string_one[i])
        else:
            total += ord(string_two[i])

print(total)