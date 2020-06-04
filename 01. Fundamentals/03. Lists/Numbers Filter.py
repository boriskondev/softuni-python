lines = int(input())

nums = []
result = []

for element in range(lines):
    nums.append(int(input()))

how_to_filter = input()

if how_to_filter == "even":
    result = [x for x in nums if x % 2 == 0]
elif how_to_filter == "odd":
    result = [x for x in nums if x % 2 != 0]
elif how_to_filter == "negative":
    result = [x for x in nums if x < 0]
elif how_to_filter == "positive":
    result = [x for x in nums if x >= 0]

print(result)