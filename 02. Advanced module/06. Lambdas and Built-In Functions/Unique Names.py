names = input().split()

valid_names = []

for name in names:
    if name[0].isupper():
        if len([True for x in name[1:] if x.islower()]) == len(name[1:]):
            valid_names.append(name)

print(sum([len(x) for x in valid_names]))
