def find_max(nums):
    largest = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > largest:
            largest = nums[i]

    return largest


nums = [4, 9, 2, 15, 7]
print(find_max(nums))
