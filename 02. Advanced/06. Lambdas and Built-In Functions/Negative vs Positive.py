numbers = [int(x) for x in input().split()]

negatives = sum([x for x in numbers if x < 0])
positives = sum([x for x in numbers if x > 0])

print(negatives)
print(positives)

if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")