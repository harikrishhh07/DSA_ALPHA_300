def sort_zero_one_two(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums

print(sort_zero_one_two([2, 0, 1, 2, 0, 1]))

