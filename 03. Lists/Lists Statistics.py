elements = int(input())

pos = []
neg = []

for element in range(elements):
    num = int(input())
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

print(pos)
print(neg)
print(f"Count of positives: {len(pos)}. Sum of negatives: {sum(neg)}")