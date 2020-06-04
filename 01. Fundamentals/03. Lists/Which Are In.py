substrings = input().split(", ")
strings = input()

chosen_ones = []

for sub in substrings:
    if sub in strings:
        chosen_ones.append(sub)

print(chosen_ones)
