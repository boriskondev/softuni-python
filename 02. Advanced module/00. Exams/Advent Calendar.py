def fix_calendar(nums):
    while True:
        shuffled = False
        for i in range(len(nums)):
            if i < len(nums) - 1:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    shuffled = True
        if not shuffled:
            break
    return nums


numbers = [3, 2, 1, 100, 5, 7]
fixed = fix_calendar(numbers)
print(fixed)
