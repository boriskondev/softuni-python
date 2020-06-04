array = []
destroyed = 0

rows = int(input())

for row in range(rows):
    nums = list(map(int, input().split()))
    array.append(nums)

attacks = input().split()

for attack in attacks:
    row, col = attack.split("-")
    row, col = int(row), int(col)
    if array[row][col] != 0:
        array[row][col] -= 1
        if array[row][col] == 0:
            destroyed += 1

print(destroyed)

