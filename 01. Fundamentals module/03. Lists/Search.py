elements = int(input())
pattern = input()

strings = []

for element in range(elements):
    strings.append(input())

pattern_found = [x for x in strings if pattern in x]

print(strings)
print(pattern_found)