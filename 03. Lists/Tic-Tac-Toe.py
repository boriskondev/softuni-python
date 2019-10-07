array = []
left_diagonal = []
right_diagonal = []
winner = ""

for row in range(3):
    nums = list(map(int, input().split()))
    array.append(nums)

horizontal = False
vertical = False
diagonal = False

for row in array:
    if len(set(row)) == 1:
        horizontal = True
        winner = row[0]

for i in range(len(array)):
    column = [row[i] for row in array]
    if len(set(column)) == 1:
        vertical = True
        winner = column[0]

left_counter = 0
right_counter = 2

for row in array:
    for i in range(len(row)):
        if i == left_counter:
            left_diagonal.append(row[i])
        if i == right_counter:
            right_diagonal.append(row[i])
    left_counter += 1
    right_counter -= 1

if len(set(left_diagonal)) == 1 or len(set(right_diagonal)) == 1:
    diagonal = True
    winner = left_diagonal[1]

if horizontal or vertical or diagonal:
    if winner == 1:
        print("First player won")
    elif winner == 2:
        print("Second player won")
    else:
        print("Draw!")
else:
    print("Draw!")
