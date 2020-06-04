num_of_chars = int(input())
counter = 0
total = 0

while counter != num_of_chars:
    total += ord(input())
    counter += 1

print(f"The sum equals: {total}")