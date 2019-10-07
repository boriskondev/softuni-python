initial_sequence = input().split()
k = int(input())

new_sequence = []

killed_counter = 0
killed = []
index_counter = 1
all_killed = False

while not all_killed:
    for index in range(len(initial_sequence)):
        if index in killed:
            continue
        if index_counter % k == 0:
            new_sequence.append(initial_sequence[index])
            killed.append(index)
            killed_counter += 1
        if killed_counter == len(initial_sequence):
            all_killed = True
            break
        index_counter += 1

print("[" + f"{','.join(new_sequence)}" + "]")