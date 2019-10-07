input_string = input().lower()

patterns = ["sand", "water", "fish", "sun"]

counter = 0

for pattern in patterns:
    counter += input_string.count(pattern)

print(counter)