str1 = [x for x in input()]
str2 = [x for x in input()]

itr = zip(str1, str2)

index = 0

for tup in itr:
    if len(tup) == len(set(tup)):
        str1[index] = tup[1]
        print("".join(str1))
    index += 1