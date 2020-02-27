def get_repeating_dna(sequence):
    matches = []
    while len(sequence) >= 11:
        sliced = sequence[:10]
        if sliced in sequence[1:] and sliced not in matches:
            matches.append(sliced)
        sequence = sequence[10:]
    return matches


test = input()

result = get_repeating_dna(test)

print(result)