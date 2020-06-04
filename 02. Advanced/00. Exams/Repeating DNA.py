def get_repeating_dna(sequence):
    matches = []
    while len(sequence) > 10:
        sliced = sequence[:10]
        if sliced in sequence[1:] and sliced not in matches:
            matches.append(sliced)
        sequence = sequence[1:]
    return matches


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"

result = get_repeating_dna(test)

print(result)