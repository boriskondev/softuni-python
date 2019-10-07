input_year = int(input()) + 1

input_year = [x for x in str(input_year)]

while len(input_year) != len(set(input_year)):
    input_year = str(int("".join(input_year)) + 1)
    input_year = [x for x in input_year]

print(int("".join(input_year)))