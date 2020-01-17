sequence = input().split(", ")
sequence = list(map(int, sequence))

filtered_sequence = list(filter(lambda x: x != 0, sequence))
to_add = len(sequence) - len(filtered_sequence)

filtered_sequence += to_add * [0]

print(filtered_sequence)