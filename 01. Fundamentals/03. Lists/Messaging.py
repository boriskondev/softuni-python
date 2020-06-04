nums = input().split()
text = input()

output = []

for num in nums:
    index = sum([int(x) for x in num])
    most_wanted_index = index % len(text)
    output.append(text[most_wanted_index])
    text = [text[i] for i in range(len(text)) if i != most_wanted_index]

print("".join(output))