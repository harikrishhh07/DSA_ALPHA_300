def wiggle_sort(nums):
    for i in range(len(nums) - 1):
        if i % 2 == 0:
            # Even index: current <= next
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            # Odd index: current >= next
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

print(wiggle_sort([3, 5, 2, 1, 6, 4]))
