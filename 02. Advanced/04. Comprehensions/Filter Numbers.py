start = int(input())
end = int(input())

target_nums = []

for num in range(start, end + 1):
    for divisor in range(2, 11):
        if num % divisor == 0:
            target_nums.append(num)
            break

print(target_nums)