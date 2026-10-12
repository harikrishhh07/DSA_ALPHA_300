def second_largest(nums):
    largest = float('-inf')
    second = float('-inf')
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and num > second:
            second = num

    if second == float('-inf'):
        return -1
    return second

nums = [-5, -2, -8, -3, -2]
print(second_largest(nums))