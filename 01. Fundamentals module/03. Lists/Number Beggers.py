numbers_list = [int(x) for x in input().split(", ")]
beggars = int(input()) * [0]

counter = 0

for num in numbers_list:
    beggars[counter] += num
    counter += 1
    if counter == len(beggars):
        counter = 0

print(beggars)