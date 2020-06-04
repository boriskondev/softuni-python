nums = list(map(int, input().split(", ")))
even_indices = [x for x in range(len(nums)) if nums[x] % 2 == 0]
print(even_indices)