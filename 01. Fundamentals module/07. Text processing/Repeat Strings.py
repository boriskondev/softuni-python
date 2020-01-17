input_string = input().split()

final = ""

for stri in input_string:
    final += stri * len(stri)

print(final)
