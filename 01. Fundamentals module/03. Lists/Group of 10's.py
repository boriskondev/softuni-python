nums = list(map(int, input().split(", ")))
step = 1

while nums:
    print(f"Group of {step}0's:", end=" ")
    filtered = [x for x in nums if x <= step * 10]
    nums = list(filter(lambda x: x not in filtered, nums))
    print(filtered)
    step += 1