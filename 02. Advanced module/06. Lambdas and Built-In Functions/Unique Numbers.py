nums = [round(float(x)) for x in input().split()]

print(min(nums))
print(max(nums))

print(" ".join(list(map(str, sorted(set([x * 3 for x in nums]))))))