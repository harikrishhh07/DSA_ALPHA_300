
def floor_ceil(nums, x):
    floor = -1
    ceil = -1
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] <= x:
            floor = nums[mid]
            lo = mid + 1
        else:
            hi = mid - 1

    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] >= x:
            ceil = nums[mid]
            hi = mid - 1
        else:
            lo = mid + 1

    return floor, ceil

print(floor_ceil([1, 2, 4, 6, 8], 5))
