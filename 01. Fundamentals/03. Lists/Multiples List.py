factor = int(input())
count = int(input())

initial_factor = factor

nums = []

for c in range(count):
    nums.append(factor)
    factor += initial_factor

print(nums)