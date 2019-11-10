dict = {}
inp_string = input()

for char in inp_string:
    if char != " ":
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

for c in dict:
    print(f"{c} -> {dict[c]}")