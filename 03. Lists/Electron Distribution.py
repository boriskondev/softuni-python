electrons = int(input())

index = 0
distributed = []

while electrons > 0:
    to_distribute = 2 * ((index+1) ** 2)
    index += 1
    if to_distribute <= electrons:
        distributed.append(to_distribute)
        electrons -= to_distribute
    else:
        distributed.append(electrons)
        electrons = 0

print(distributed)