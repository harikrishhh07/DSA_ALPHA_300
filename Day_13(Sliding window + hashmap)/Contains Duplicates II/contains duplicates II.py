def containsNearbyDuplicate(nums, k):
    seen = set()
    for i, x in enumerate(nums):
        if x in seen:
            return True
        seen.add(x)
        if i >= k:
            seen.remove(nums[i - k])
    return False